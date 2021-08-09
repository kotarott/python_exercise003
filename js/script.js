$("#search").on("click", function(){
    const keyword = $("#keyword").val()
    if (!keyword) {
        alert("検索ワードを入力してください。")
        return
    }
})