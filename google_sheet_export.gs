
function exportLatestRow() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Sheet1");
  const lastRow = sheet.getLastRow();
  const data = sheet.getRange(lastRow, 1, 1, sheet.getLastColumn()).getValues();
  Logger.log(JSON.stringify(data[0]));
}
