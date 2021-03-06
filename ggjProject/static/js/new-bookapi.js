/* new.html 파일에 들어가는 도서검색 API 처리 js 파일입니다. */

// book 검색 자동완성
$(document).ready(function () {
    $('#bookSearch').keyup(function () {
        if ($(this).val() == '') {
            $("#bookResult *").remove();
            $('#bookResult').append('<p class="exception">검색어를 입력해주세요 </p>')
        } else {
            $('#bookResult').html('');
            var searchField = $('#bookSearch').val();
            $.ajaxSetup({
                method: "GET",
                data: {
                    query: $("#bookSearch").val()
                },
                headers: {
                    Authorization: "KakaoAK ea6f4522facf69c938f433e154fd99a1"
                }
            })
            $.getJSON('https://dapi.kakao.com/v3/search/book?', function (bookData) {
                $("#bookResult *").remove();
                $.each(bookData, function (key, value) {
                    if (value.length == 0) {
                        $('#bookResult').append('<p class="exception">검색결과가 없습니다 </p>')
                    } else {
                        console.log(bookData);
                        if (value.length == 1) {
                            $('#bookResult').css("max-height", "200px");
                        } else {
                            $('#bookResult').css("max-height", "320px");
                        }
                        for (var j = 0; j < value.length; j++) {
                            var toObj = new Object;
                            toObj.thumbnail = value[j].thumbnail;
                            toObj.title = value[j].title.replace("\'","’");
                            toObj.isbn = value[j].isbn;
                            toObj.authors = value[j].authors;
                            toObj.publisher = value[j].publisher;
                            toObj.datetime = value[j].datetime;

                            var toObjc = new Object;
                            toObjc.contents = value[j].contents;
                            // var info = new Array();
                            // info[0] = value[j].title;
                            // info[1] = value[j].isbn;
                            // info[2] = value[j].thumbnail;
                            // info[3] = value[j].authors;
                            // info[4]  = value[j].publisher;
                            // info[5]  = value[j].datetime;
                            // info[6]  = value[j].contents;

                            // var info = "";
                            // info = [{"title": value[j].title, "isbn" : value[j].isbn, "thumbnail": value[j].thumbnail}]
                            let data = JSON.stringify(toObj)//.replace("\'","’");
                            let datac = JSON.stringify(toObjc)
                            var datadata = value[j].contents;
                            //console.log(value[j]);
                            $('#bookResult').append('<div class="book_item" id=' + "'" + data 
                            + "' value1=" + "'" + value[j].thumbnail 
                            + "' value2 = " + "'" + value[j].title 
                            + "' value3 = " + "'" + value[j].isbn 
                            + "' value4 = " + "'" + value[j].authors 
                            + "' value5 = "+"'" + value[j].publisher 
                            + "' value6 = " + "'" + value[j].datetime 
                            + "' value7 = " + "'" + value[j].contents 
                            + "'"+ ' onclick="showSelectBook(this)">' +
                                '<img src="' + toObj.thumbnail + '" class="thumbnail" />' + '<div class="book_infos">' +
                                '<p class="book_info title noto-medium">' + toObj.title + '</p>' +
                                '<p class="book_info authors noto-light">' + toObj.authors + ' 지음</p>' +
                                // '<p class="contents">' + value[j].contents + '</p>' +
                                '<p class="book_info publisher noto-light">' + toObj.publisher + '</p>' +
                                '<p class="book_info datetime noto-light">' + strToDate(toObj.datetime) + '</p>' +
                                '</div>' + '</div>')

                            // $('#bookResult').append('<li>'+value[j].title+value[j].authors+
                            // value[j].thumbnail+value[j].contents+value[j].publisher+'</li>')
                        }
                    }
                })
            })
        }

    });
});

const strToDate = (obj) => {
    let year = obj.substring(0, 4);
    let month = obj.substring(5, 7);
    return `${year}년 ${month}월`;
}

