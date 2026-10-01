param(
    [switch]$RequireComplete
)

$ErrorActionPreference = 'Stop'
$projectRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$trackerPath = Join-Path $projectRoot 'docs/implementacion/seguimiento.csv'
$matrixPath = Join-Path $projectRoot 'docs/implementacion/04_matriz_aceptacion.md'
$evidenceRoot = [IO.Path]::GetFullPath((Join-Path $projectRoot 'docs/implementacion/evidencias'))
$rows = @(Import-Csv -LiteralPath $trackerPath -Encoding UTF8)
$acceptanceIds = @{}
foreach ($line in (Get-Content -LiteralPath $matrixPath -Encoding UTF8)) {
    if ($line -match '^\| (A\d{2}) \|') { $acceptanceIds[$Matches[1]] = $true }
}
$allowed = @('pendiente', 'en_progreso', 'bloqueado', 'en_revision', 'completado')
$gates = @('G0', 'G1', 'G2', 'G3', 'G4', 'G5')
$errors = [System.Collections.Generic.List[string]]::new()
$byId = @{}

if ($rows.Count -eq 0) { $errors.Add('El seguimiento no contiene tareas.') }
foreach ($row in $rows) {
    if ([string]::IsNullOrWhiteSpace($row.id)) { $errors.Add('Hay una tarea sin ID.'); continue }
    if ($byId.ContainsKey($row.id)) { $errors.Add("ID repetido: $($row.id)") }
    else { $byId[$row.id] = $row }
    if ($allowed -notcontains $row.status) { $errors.Add("Estado invalido en $($row.id): $($row.status)") }
    if ($gates -notcontains $row.gate) { $errors.Add("Puerta invalida en $($row.id): $($row.gate)") }
    if ([string]::IsNullOrWhiteSpace($row.title)) { $errors.Add("Falta titulo en $($row.id)") }
    if ($row.acceptance_ids -notmatch '^A\d{2}(\|A\d{2})*$') { $errors.Add("Criterios invalidos en $($row.id)") }
    else {
        foreach ($criterion in ($row.acceptance_ids -split '\|')) {
            if (-not $acceptanceIds.ContainsKey($criterion)) { $errors.Add("Criterio desconocido en $($row.id): $criterion") }
        }
    }
    if ($row.last_updated -notmatch '^\d{4}-\d{2}-\d{2}$') { $errors.Add("Falta fecha de actualizacion en $($row.id)") }
}

foreach ($row in $rows) {
    $deps = @($row.depends_on -split '\|' | Where-Object { $_ -ne '' })
    foreach ($dep in $deps) {
        if (-not $byId.ContainsKey($dep)) { $errors.Add("Dependencia desconocida: $($row.id) -> $dep") }
        elseif ($dep -eq $row.id) { $errors.Add("Autodependencia en $($row.id)") }
        elseif ($row.status -eq 'completado' -and $byId[$dep].status -ne 'completado') {
            $errors.Add("$($row.id) figura completada antes de $dep")
        }
    }

    if ($row.status -eq 'completado') {
        if ([string]::IsNullOrWhiteSpace($row.reviewer)) { $errors.Add("Falta revisor de $($row.id)") }
        if ($row.reviewed_at -notmatch '^\d{4}-\d{2}-\d{2}$') { $errors.Add("Falta fecha ISO de revision de $($row.id)") }
        else {
            try { [void][datetime]::ParseExact($row.reviewed_at, 'yyyy-MM-dd', [Globalization.CultureInfo]::InvariantCulture) }
            catch { $errors.Add("Fecha de revision invalida en $($row.id)") }
        }
        $paths = @($row.evidence_paths -split '\|' | Where-Object { $_ -ne '' })
        if ($paths.Count -eq 0) { $errors.Add("Falta evidencia de $($row.id)") }
        foreach ($relativePath in $paths) {
            $absolutePath = [IO.Path]::GetFullPath((Join-Path $projectRoot $relativePath))
            if (-not $absolutePath.StartsWith($evidenceRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
                $errors.Add("Evidencia fuera del directorio permitido: $($row.id) -> $relativePath")
            }
            elseif (-not (Test-Path -LiteralPath $absolutePath -PathType Leaf)) {
                $errors.Add("Evidencia inexistente: $($row.id) -> $relativePath")
            }
        }
    }
}

if ($errors.Count -gt 0) {
    foreach ($message in $errors) { Write-Error $message }
    exit 1
}

$done = @($rows | Where-Object { $_.status -eq 'completado' }).Count
$percent = [math]::Round(100 * $done / $rows.Count, 1)
Write-Output "Seguimiento valido: $done/$($rows.Count) tareas completas ($percent%)."
$allGatesComplete = $true
foreach ($gate in $gates) {
    $members = @($rows | Where-Object { $_.gate -eq $gate })
    $completed = @($members | Where-Object { $_.status -eq 'completado' }).Count
    $gateComplete = $members.Count -gt 0 -and $completed -eq $members.Count
    if (-not $gateComplete) { $allGatesComplete = $false }
    $label = if ($gateComplete) { 'APROBADA' } else { 'PENDIENTE' }
    Write-Output "$gate $label ($completed/$($members.Count))"
}

if ($RequireComplete -and -not $allGatesComplete) { exit 2 }
exit 0
