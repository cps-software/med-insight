<?php
// Entry point for the backend
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
