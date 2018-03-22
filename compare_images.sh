
name="_result.txt"
result="$1$name"

echo -n "215 original vs 215 original = " >>"$result"
/usr/local/bin/compare -metric SSIM 215/original/$1/image_default.png 215/original/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >>"$result"
echo -n "215 original vs 215 lowered = " >>"$result"
/usr/local/bin/compare -metric SSIM 215/original/$1/image_default.png 215/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"
echo -n "215 original vs 218 orignal = " >> "$result"
/usr/local/bin/compare -metric SSIM 215/original/$1/image_default.png 218/original/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"
echo -n "215 original vs 218 lowered = " >> "$result"
/usr/local/bin/compare -metric SSIM 215/original/$1/image_default.png 218/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"

echo -n "218 original vs 218 original = " >> "$result"
/usr/local/bin/compare -metric SSIM 218/original/$1/image_default.png 218/original/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"
echo -n "218 original vs 218 lowered = " >> "$result"
/usr/local/bin/compare -metric SSIM 218/original/$1/image_default.png 218/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"
echo -n "218 original vs 215 lowered" >> "$result"
/usr/local/bin/compare -metric SSIM 218/original/$1/image_default.png 215/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"

echo -n "215 lowered vs 215 lowered = " >> "$result"
/usr/local/bin/compare -metric SSIM 215/lowered/$1/image_default.png 215/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"
echo -n "215 lowered vs 218 lowered = " >> "$result"
/usr/local/bin/compare -metric SSIM 215/lowered/$1/image_default.png 218/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"

echo -n "218 lowered vs 218 lowered = " >> "$result"
/usr/local/bin/compare -metric SSIM 218/lowered/$1/image_default.png 218/lowered/$1/image_default.png barcelona_diff_machines.png 2>>"$result"
echo "" >> "$result"








