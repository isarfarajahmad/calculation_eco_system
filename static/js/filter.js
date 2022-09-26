function filter() {
  var FilterValue, input, ul, li, i;

  input = document.getElementById("search");
  FilterValue = input.nodeValue.toLowerCase();
  ul = document.getElementById("menu");
  li = ul.getElementsByTagName("tbody");

  for (i = 0; i < li.length; i++) {
    var a = li[i].getElementsByTagName("tr")[0];
    if (a.innerHTML.toLowerCase().indexOf(FilterValue) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
