# GitHub Action: Feature Badge
Diese GitHub Action liefert eine GitHub Badge als Indikator dafür, wie viele Features bereits auf Staging, aber noch nicht auf Production aktiv sind.
Die Badge wird standardmäßig in die README.md eines Projekts eingefügt, es kann aber auch ein anderer Dateipfad angegeben werden.
Ein Klick auf die Badge führt zu einer Übersicht der Actions, die auf `main` gelaufen sind. Dabei sieht man dann auf einen Blick, wie viele Deployment Updates es seit der letzten Promotion gab.
Die Feature Badge Action kann auf zwei Arten genutzt werden: Entweder die Differenz der Features wird um eins hochgezählt, oder sie wird zurückgesetzt.
Es empfiehlt sich, das Hochzählen an ein Deployment Update zu koppeln und das Zurücksetzen an eine Promotion nach Production.

## Badges

Es gibt drei verschiedene Zustände, die durch Badges dargestellt werden:

1. ![Feature Diff](https://img.shields.io/badge/feature%20diff-up%20to%20date-33CD56.svg): Staging und Production sind auf dem gleichen Stand.
2. ![Feature Diff](https://img.shields.io/badge/feature%20diff-prod%20one%20feature%20behind-FFFF00.svg): Es gibt ein Deployment Update, welches noch nicht promoted wurde.
3. ![Feature Diff](https://img.shields.io/badge/feature%20diff-prod%20more%20than%20one%20feature%20behind-eb4034.svg): Es gibt mehr als ein Deployment Update, welches noch nicht promoted wurde.

## Inputs

Es können vier Inputs definiert werden:
- **method** (optional):
    - Entweder `bump`, um die Differenz hochzuzählen oder `reset`, um die Differenz zurückzusetzen. Default: `bump`.
- **file_path** (optional):
    - Der Pfad zu der Datei, in die die Badge eingefügt werden soll. Default: `README.md`.
- **project_name**:
    - Der Name des Projekts, in dem die Action genutzt wird. Wird benötigt, um den Link der Badge richtig zu setzen. Kann generisch über Umgebungsvariablen der aufrufenden GitHub Action gesetzt werden: `${{ github.event.repository.name }}`.
- **branch_name** (optional):
    - Hier kann ein Branch angegeben werden, in dem die Badge gesetzt werden soll. Diese Funktion ist hauptsächlich für das Ausprobieren der Action gedacht. Default: `main`.

## Beispiele

Hochzählen der Differenz:

    jobs:
        <job_name>:
            name: <name>
            needs: <deployment update>
            runs-on: [self-hosted, x64, linux, ephemeral, zon-image-latest]
            steps:
            - uses: ZeitOnline/gh-action-feature-badge@main
                with:
                    project_name: ${{ github.event.repository.name }}

Zurücksetzen der Differenz:

    jobs:
        <job_name>:
            name: <name>
            needs: <promotion to production>
            runs-on: [self-hosted, x64, linux, ephemeral, zon-image-latest]
            steps:
            - uses: ZeitOnline/gh-action-feature-badge@main
                with:
                    project_name: ${{ github.event.repository.name }}
                    method: reset
