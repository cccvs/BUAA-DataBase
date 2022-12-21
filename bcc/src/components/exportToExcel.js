function transform(table, name, callback) {  //table为表格数据,name为导出文件名,
    let tableInnerHTML = ''
    let headerData = ['序号','姓名','年龄','性别','爱好','发量','薪水'] //定义列名
    let bodyData = table
    tableInnerHTML += '<thead><tr>';
    tableInnerHTML += `<th colspan=${headerData.length} 
    				style='background:#CCFFFF;border:solid;'>` + name + "</th></tr>"
    tableInnerHTML += '<tr>'
    headerData.forEach(item => {
        tableInnerHTML += "<th rowspan='1' style='background:#FFFFCC;border:solid'>"
            + item + "</th>"
    })
    tableInnerHTML += '</tr></thead>';
    tableInnerHTML += '<tbody>'
    bodyData.forEach(item => {
        tableInnerHTML += "<tr>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.index + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.name + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.age + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.sex + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.hobby + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.hair + "</td>"
        tableInnerHTML += "<td align='center' style='border:solid'>" + item.salaried + "</td>"
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
