
*****************************LOCAL GOVERNMENTS********************************
cd ""
**PIM1:
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
import excel using `x'_LOC_PIM1_`i'.xlsx, clear sheet("Sheet1") first
gen Mes=.
replace Mes=12 if `i'==2019|`i'==2018|`i'==2017
save PIM1_`i'_`x'.dta,replace
	}
	}
	
**DV1:
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
import excel using `x'_LOC_DV1_`i'.xlsx, clear sheet("Sheet1") first
save DV1_`i'_`x'.dta,replace
	}
	}
	
**MERGE PIM1 & DV1
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
use  PIM1_`i'_`x'.dta, clear
merge 1:1 ID using DV1_`i'_`x'.dta
save DV1_PIM1_`i'_`x'.dta,replace

	}
	}

**DV 2
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
import excel using `x'_LOC_CONSTR_DV2_`i'.xlsx, clear sheet("Sheet1") first
rename D_SGEspecifica code_subcat
gen ID2= ID+code_subcat
save DV2_`i'_`x'.dta,replace
	}
	}
	
**PIM2
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
import excel using `x'_LOC_CONSTR_PIM2_`i'.xlsx, clear sheet("Sheet1") first
rename D_SGEspecifica code_subcat
gen ID2= ID+code_subcat
gen Mes=.
replace Mes=12 if `i'==2019|`i'==2018|`i'==2017
save PIM2_`i'_`x'.dta,replace
	}
	}
	
**MERGE PIM2 & DV2
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
use PIM2_`i'_`x'.dta, clear
duplicates report ID2
merge 1:1 ID2 using DV2_`i'_`x'.dta
drop _merge
save DV2_PIM2_`i'_`x'.dta,replace
	}
	}

**MERGE ALL
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
use DV1_PIM1_`i'_`x'.dta,clear
drop _merge
duplicates report ID
merge 1:m ID using DV2_PIM2_`i'_`x'.dta
drop _merge ID2
save PREV_LOC_`i'_`x'.dta,replace
	}
	}

**PROCESSING DUPLICATES
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
use PREV_LOC_`i'_`x'.dta,clear
sort ID
quietly by ID:  gen dup = cond(_N==1,0,_n)
replace PIM_1=. if dup>=2
replace Dv_1=. if dup>=2
drop dup code_subcat ID
save LOCAL_`i'_`x'.dta,replace
	}
	}
	
**TO EXCEL
foreach x in "AM" "PIU" "LAM" "TUM"{
    foreach i of numlist 2017/2019 {
use LOCAL_`i'_`x'.dta,clear
export excel using LOCAL_`i'_`x'.xlsx, firstrow(variables) replace
	}
	}
***********************NATIONAL AND REGIONAL GOVERNMENT*********************
cd "" 

**PIM1:
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
import excel using `x'_PIM1_`i'.xlsx, clear sheet("Sheet1") first
gen Mes=.
replace Mes=12 if `i'==2019|`i'==2018|`i'==2017
save PIM1_`i'_`x'.dta,replace
	}
	}
	
**DV1:
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
import excel using `x'_DV1_`i'.xlsx, clear sheet("Sheet1") first
save DV1_`i'_`x'.dta,replace
	}
	}
	
**MERGE PIM1 & DV1
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
use  PIM1_`i'_`x'.dta, clear
merge 1:1 ID using DV1_`i'_`x'.dta, update
save DV1_PIM1_`i'_`x'.dta,replace

	}
	}

**DV 2
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
import excel using `x'_DV2_`i'.xlsx, clear sheet("Sheet1") first
gen ID2=ID+Categoría
save DV2_`i'_`x'.dta,replace
	}
	}
	
**PIM2
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
import excel using `x'_PIM2_`i'.xlsx, clear sheet("Sheet1") first
gen Mes=.
replace Mes=12 if `i'==2019|`i'==2018|`i'==2017
gen ID2=ID+Categoría
save PIM2_`i'_`x'.dta,replace
	}
	}

**MERGE DV2 & PIM2
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
use PIM2_`i'_`x'.dta, clear
merge 1:1 ID2 using DV2_`i'_`x'.dta, update
drop _merge
save DV2_PIM2_`i'_`x'.dta,replace
	}
	}
	
**MERGE ALL
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
use DV1_PIM1_`i'_`x'.dta,clear
drop _merge
duplicates report ID
merge 1:m ID using DV2_PIM2_`i'_`x'.dta,force
drop _merge ID2
save PREV_`i'_`x'.dta,replace
	}
	}

**PROCESSING DUPLICATES
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
use PREV_`i'_`x'.dta,clear
sort ID
quietly by ID:  gen dup = cond(_N==1,0,_n)
replace PIM_1=. if dup>=2
replace Dv_1=. if dup>=2
drop dup ID D_SGEspecifica NombredeNiveldeGobierno
save `i'_`x'.dta,replace
	}
	}

**TO EXCEL
foreach x in "NAC" "REG"{
    foreach i of numlist 2017/2019 {
use `i'_`x'.dta,clear

export excel using `i'_`x'.xlsx, firstrow(variables) replace
	}
	}
