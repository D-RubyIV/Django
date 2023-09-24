var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    var dropdownIcon = this.querySelector(".dropdown");
    var dropupIcon = this.querySelector(".dropup");

    if (content.style.display === "block") {
      content.style.display = "none";
      dropdownIcon.style.display = "block";
      dropupIcon.style.display = "none";
    } else {
      content.style.display = "block";
      dropdownIcon.style.display = "none";
      dropupIcon.style.display = "block";
    }
  });
}
function toggleCopyIcon(ele, button) {
 
  
  var copyToken = button.closest(".url-content");
  copyToClipboard(ele, copyToken);
  var icon1 = copyToken.querySelector(".icon1");
  var icon2 = copyToken.querySelector(".icon2");

  if (icon1.style.display == "block") {
    icon1.style.display = "none";
    icon2.style.display = "block";
  }
  
  callbackIcon(copyToken);
}

async function callbackIcon(copyToken) {
  await new Promise(resolve => setTimeout(resolve, 1000)); // Đợi 2 giây
  var icon1 = copyToken.querySelector(".icon1");
  var icon2 = copyToken.querySelector(".icon2");
  icon1.style.display = "block";
  icon2.style.display = "none";
}


function copyToClipboard(ele, choiceDiv) {
  // Get the text field
  const tokenParagraph = choiceDiv.querySelector(ele);
  const range = document.createRange();
  range.selectNode(tokenParagraph);
  // Select the content of the paragraph
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  // Use the Clipboard API to copy the selected content to the clipboard
  document.execCommand('copy');
  // Remove the range to clear the selection
  window.getSelection().removeAllRanges();
  // Provide feedback to the user

}


