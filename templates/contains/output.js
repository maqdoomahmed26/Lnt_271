

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
                console.log('Updating dg_input row:', index, 'Value:', item);
                rows[index].cells[2].innerHTML = item;
            } else {
                console.log('No row found at index', index, 'for dg_input');
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
                console.log('Updating an_input row:', index, 'Value:', item);
                rows[index].cells[2].innerHTML = item;
            } else {
                console.log('No row found at index', index, 'for an_input');
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
                console.log('Updating dg_output row:', index, 'Value:', item);
                rows[index].cells[3].innerHTML = item;
            } else {
                console.log('No row found at index', index, 'for dg_output');
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
                console.log('Updating an_output row:', index, 'Value:', item);
                rows[index].cells[3].innerHTML = item;
            } else {
                console.log('No row found at index', index, 'for an_output');
            }
        });
    }