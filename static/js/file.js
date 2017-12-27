/**
 * Created by administrator on 2017/12/26.
 */

//上传文件函数
function upload_file(file_path,file_obj,return_location){
    var file_data = new FormData()
    file_data.append('relpath', JSON.stringify(file_path))
    file_data.append('file_obj',file_obj)
    $.ajax({
        url: '/file/',
        type: 'POST',
        data: file_data,
        processData: false,
        contentType: false,
        success: function (msg) {
            if ( msg == 'OK' ){
                return_location.text('上传成功')
            }else if( msg == 'failed'){
                return_location.text('上传失败')
            }else if( msg == 'exists'){
                return_location.text('文件已存在')
            }
        }
    })
}

//新建目录
function new_dir_func(file_path,new_dir_name,return_location){
    file_path.push(new_dir_name)
    console.log(file_path)
    $.ajax({
        url: 'file.html',
        type: 'POST',
        data: {new_dir_data:JSON.stringify(file_path)},
        success: function (msg) {
            if ( msg == 'OK' ){
                return_location.text('新建成功')
            }else if( msg == 'failed'){
                return_location.text('新建失败')
            }else if( msg == 'exists'){
                return_location.text('文件夹已存在')
            }
        }
    })
}

//给返回的文件和文件夹数据展示函数
function data_show(data){
    for ( var dir in data['dir']){
        var dir_name = data['dir'][dir]
        var dir_lable = '<li class="list-group-item"><input type="checkbox" ><a class="list_dir" onclick="change_dir(this)" dir="'+dir_name+'"> '+' '+ dir_name+'</a></li>'
        $('#file_list').append(dir_lable)
    }
    for ( var file in data['file']){
        var file_name = data['file'][file]
        var file_lable = '<li class="list-group-item"><input type="checkbox" value="'+file_name+'">'+' '+file_name+'</li>'
        $('#file_list').append(file_lable)
    }

    for ( var relpaht in data['relpath'] ){
        var finally_dir =  data['relpath'][relpaht]
        if ( finally_dir != '' ){
            var relpath_lable = '<li name="sub" ><a class="path_dir"  onclick="change_path(this)" path_dir="'+finally_dir+'">'+finally_dir+'</a></li>'
            $('#relpath').append(relpath_lable)
        }
    }
}