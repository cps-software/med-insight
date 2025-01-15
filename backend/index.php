<?php
/*
|----------------------------------------------------------------------
| index.php
|----------------------------------------------------------------------
| Entry point for the backend.
| Returns simple JSON message with API info.
| Start a PHP server on a designated port for frontend to call, e.g.:
| http://localhost:8000
|
*/

header('Content-Type: application/json');

echo json_encode([
  'status' => 'success',
  'message' => 'MedInsight backend is operational.',
  'endpoints' => [
    '/api/auth.php',
    '/api/records.php',
    '/api/analysis.php',
    '/api/insights.php',
    '/api/tracking.php'
  ]
]);
