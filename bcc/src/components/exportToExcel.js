function transform(table, name, callback) {  //table为表格数据,name为导出文件名,
    let tableInnerHTML = ''
    /*
    TODO:确定列名
     */
    let headerData = ['用户ID','姓名','头像','社内职务'] //定义列名
    let bodyData = table
    headerData.forEach(item => {
        tableInnerHTML += "<th rowspan='1' style='background:#FFFFCC;border:solid'>"
            + item + "</th>"
    })
    tableInnerHTML += '</tr></thead>';
    tableInnerHTML += '<tbody>'
    bodyData.forEach(item => {
        tableInnerHTML += "<tr>"
        /*
        TODO: 每列对应的数据的具体键值
         */
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.user_id + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.real_name + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.avatar + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.label + "</td>"
        tableInnerHTML += "</tr>"
    })
    tableInnerHTML += '</tbody>';    //身体结束
    function getExplorer() {
        let explorer = window.navigator.userAgent;
        if (explorer.indexOf('MSIE') >= 0) {
            return 'ie';        // ie
        } else if (explorer.indexOf('Firefox') >= 0) {
            return 'Firefox';   // firefox
        } else if (explorer.indexOf('Chrome') >= 0) {
            return 'Chrome';    // Chrome
        } else if (explorer.indexOf('Opera') >= 0) {
            return 'Opera';     // Opera
        } else if (explorer.indexOf('Safari') >= 0) {
            return 'Safari';    // Safari
        }
    }

    if (getExplorer() !== 'Safari' && name.substr(-1, 4) !== '.xls') {
        name += '.xls';
    }
    tableToExcel(tableInnerHTML, name, callback);
}

let tableToExcel = (function () {
    let template = '<html><head><meta charset="UTF-8"></head><body><table>{table}</table></body></html>';
    let format = function (s, c) {
        return s.replace(/{(\w+)}/g, function (m, p) { return c[p]; });
    };
    return function (table, name, callback) {
        let ctx = { worksheet: name || 'Worksheet', table: table };
        let blob = new Blob([format(template, ctx)]);
        let a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = name;
        a.click();
        a.remove();
        callback('success');
    };
})();
export default transform;
