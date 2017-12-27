/**
 * Created by Administrator on 2017/12/18.
 */

function data_show(data){
    var content = $('#content')
    content.empty()
    var i = 1
    for ( var host in data ){
        if (data[host] == true){
            var rows = '<tr class="success"><td>'+i+'</td><td>'+host+'</td><td>' +data[host]+'</td></tr>'
            content.append(rows)
            i++
        }else if (data[host] == false){
            var rows = '<tr class="danger"><td>'+i+'</td><td>'+host+'</td><td>' +data[host]+'</td></tr>'
            content.append(rows)
            i++
        }else{
            var rows = '<tr class="success"><td>'+i+'</td><td>'+host+'</td><td>' +data[host]+'</td></tr>'
            content.append(rows)
            i++
        }
    }
}



