// Version : 1.0.0.00
// Date : 2024/07/06 09:30
// Author : Long17369
// 用于记录访问
emailjs.init('STvl-WKywqVLU_B86')
const serviceID = 'default_service';
const templateID = 'template_h89p3lj';
fetch('https://api.ipify.org?format=json')
    .then(response => response.json())
    .then(data => {
        console.log(data.ip)
        emailjs.sendForm("service_7rui72a", "template_h89p3lj", {
            ip: data.ip,
            source: "456",
        })
    })
    .catch(error => console.error('Unable to get IP address:', error));
