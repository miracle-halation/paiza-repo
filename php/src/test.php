<?php
$attendance_date = intval(fgets(STDIN));

if ($attendance_date < 1 || 10000 < $attendance_date) {
	exit();
}

$works = array();
for ($i = 1; $i <= $attendance_date; $i++) {
	$work = explode(" ", fgets(STDIN));
	if (count($work) !== 2) {
		exit();
	}
	if ($work[0] < 1 || 100000 < $work[0]) {
		exit();
	}
	if ($work[1] < 1 || 100000 < $work[1]) {
		exit();
	}
	$works[] = $work;
}

$min = 1;
$max = 0;
$continue_attendance = 0;
$cnt_works = count($works);

foreach ($works as $value) {
	$standard_key_array[] = $value[0];
}
array_multisort($standard_key_array, SORT_ASC, $works);

foreach ($works as $value) {
	$max_plus = $max + 1;
	if ($max < $value[1]) {
		$max = $value[1];
	}
	if ($max_plus < $value[0]) {
		$min = $value[0];
	}
	$count = $max - $min + 1;
	if ($continue_attendance < $count) {
		$continue_attendance = $count;
	}
}

echo round($continue_attendance) . "\n";
