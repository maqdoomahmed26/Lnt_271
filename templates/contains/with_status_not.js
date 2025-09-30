 // Ensure the tables are available and have tbody
 let dgInputTable = document.getElementById('dg_input').getElementsByTagName('tbody')[0];
 let anInputTable = document.getElementById('an_input').getElementsByTagName('tbody')[0];
 let dgOutputTable = document.getElementById('dg_output').getElementsByTagName('tbody')[0];
 let anOutputTable = document.getElementById('an_output').getElementsByTagName('tbody')[0];

 if (!dgInputTable || !anInputTable || !dgOutputTable || !anOutputTable) {
     console.error('Table bodies not found!');
     return;
 }

 // Update values in the dg_input table (LnT_V)
 if (Array.isArray(data.value_dg_input)) {
     let rows = dgInputTable.rows;
     console.log('Updating dg_input table...');
     data.value_dg_input.forEach((item, index) => {
         if (rows[index]) {
             // Update the LnT_V column (index 2)
             rows[index].cells[2].innerHTML = item;

             // Compare LnT_V and Ref_V, and set the status
             let refVal = data.value_dg_output[index];  // Assuming this is the Ref_V value
             let statusCell = rows[index].cells[4];  // Status column

             if (item === refVal) {
                 statusCell.innerHTML = "Pass";
                 statusCell.style.backgroundColor = "green";
                 statusCell.style.color = "white";
             } else {
                 statusCell.innerHTML = "Fail";
                 statusCell.style.backgroundColor = "red";
                 statusCell.style.color = "white";
             }
         }
     });
 }

 // Update values in the an_input table (LnT_V)
 if (Array.isArray(data.value_an_input)) {
     let rows = anInputTable.rows;
     console.log('Updating an_input table...');
     data.value_an_input.forEach((item, index) => {
         if (rows[index]) {
             // Update the LnT_V column (index 2)
             rows[index].cells[2].innerHTML = item;

             // Calculate upper and lower bounds for Ref_V ±10%
             let refVal = parseFloat(data.value_an_output[index]);  // Assuming this is the Ref_V value
             let lowerBound = refVal * 0.98;  // Lower bound is Ref_V - 2%
             let upperBound = refVal * 1.02;  // Upper bound is Ref_V + 2%
             let statusCell = rows[index].cells[4];  // Status column

             if (item > lowerBound && item < upperBound) {
                 statusCell.innerHTML = "Pass";
                 statusCell.style.backgroundColor = "green";
                 statusCell.style.color = "white";
             } else {
                 statusCell.innerHTML = "Fail";
                 statusCell.style.backgroundColor = "red";
                 statusCell.style.color = "white";
             }
         }
     });
 }

 // Update values in the dg_output table (Ref_V)
 if (Array.isArray(data.value_dg_output)) {
     let rows = dgOutputTable.rows;
     console.log('Updating dg_output table...');
     data.value_dg_output.forEach((item, index) => {
         if (rows[index]) {
             // Update the Ref_V column (index 3)
             rows[index].cells[3].innerHTML = item;

             // Compare LnT_V and Ref_V and set the status
             let lnTVal = data.value_dg_input[index];  // Assuming this is the LnT_V value
             let statusCell = rows[index].cells[4];  // Status column

             if (lnTVal !== item) {
                 statusCell.innerHTML = "Pass";
                 statusCell.style.backgroundColor = "green";
                 statusCell.style.color = "white";
             } else {
                 statusCell.innerHTML = "Fail";
                 statusCell.style.backgroundColor = "red";
                 statusCell.style.color = "white";
             }
         }
     });
 }

 // Update values in the an_output table (Ref_V)
 if (Array.isArray(data.value_an_output)) {
     let rows = anOutputTable.rows;
     console.log('Updating an_output table...');
     data.value_an_output.forEach((item, index) => {
         if (rows[index]) {
             // Update the Ref_V column (index 3)
             rows[index].cells[3].innerHTML = item;
             // rows[index].cells[2].innerHTML = item2;

             // Calculate upper and lower bounds for LnT_V ±10%
             let lnTVal = parseFloat(data.value_an_input[index]);  // Assuming this is the LnT_V value
             let lowerBound = lnTVal * 0.98;  // Lower bound is LnT_V - 2%
             let upperBound = lnTVal * 1.02;  // Upper bound is LnT_V + 2%
             let statusCell = rows[index].cells[4];  // Status column

             if (item > lowerBound && item < upperBound) {
                 statusCell.innerHTML = "Pass";
                 statusCell.style.backgroundColor = "green";
                 statusCell.style.color = "white";
             } else {
                 statusCell.innerHTML = "Fail";
                 statusCell.style.backgroundColor = "red";
                 statusCell.style.color = "white";
             }
         }
     });
 }