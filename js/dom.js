
export function pageLoad() {
// Create a form element
var form = document.createElement("form");

// Create a table element
var table = document.createElement("table");

// Create and append rows to the table
for (var j = 0; j < 16; j++) {
    var row = document.createElement("tr");

    // Create and append cells to the row
    for (var i = 0; i < 4; i++) {
        var cell = document.createElement("td");

        if (i === 0) {
            // First column contains text "Significant Other" for all rows
            cell.textContent = "Significant Other";
        } else {
            // Create input element for the remaining cells
            var input = document.createElement("input");
            input.type = "text";
            cell.appendChild(input);
        }

        // Append the cell to the row
        row.appendChild(cell);
    }

    // Append the row to the table
    table.appendChild(row);
}

// Create a submit button
var submitButton = document.createElement("input");
submitButton.type = "submit";
submitButton.value = "Submit";

// Append the submit button to the form
form.appendChild(table);
form.appendChild(submitButton);

// Append the form to the body
document.body.appendChild(form);



//Adds the image
let chartImage = document.createElement("img");
chartImage.id = "chartImage";
chartImage.src = "img/visual.png";
document.body.appendChild(chartImage);
}