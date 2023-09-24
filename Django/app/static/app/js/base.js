document.addEventListener("DOMContentLoaded", function () {
    showMessageEventLoad()
});

function showMessageEventLoad(){
    const notifications = document.querySelectorAll(".notification");
    notifications.forEach(function (notification, index) {
        setTimeout(function () {
            notification.style.opacity = "1"; // Rõ dần
            notification.style.transform = "translateX(0)"; // Xuất hiện từ phải sang
            setTimeout(function () {
                notification.style.opacity = "0"; // Mờ dần
                notification.style.transform = "translateX(100%)"; // Biến mất vào lề bên phải
                setTimeout(function () {
                    notification.style.display = "none"; // Biến mất hoàn toàn
                }, 1000); // Thời gian mờ dần
            }, 4000); // Thời gian hiển thị
        }, index * 300); // Thời gian delay
    });
}



function copyToClipboard(ele) {
    // Get the text field
    const tokenParagraph = document.getElementById(ele);
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
    alert('Token copied to clipboard');

}