const search = document.querySelector(".searchbutton");
const weatherContainer = document.querySelector(".weathercontainer");


search.addEventListener("click", () => {
    const apikey = "881f42184ba7ded96cec95f6c1573ddb";
    const city = document.querySelector(".searchcontainer input").value;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apikey}`)
        .then(response => response.json())
        .then(json => {
            if (json.cod !== 200) {
                displayError();
                return;
            }

            const image = document.querySelector(".weathercontainer img");
            const temp = document.querySelector(".weathercontainer .temp");
            const content = document.querySelector(".weathercontainer .content");
            const todayDate = document.querySelector(".weathercontainer .today");

            temp.innerHTML = `${json.main.temp} <span>°C</span>`;
            content.textContent = json.weather[0].description;
            todayDate.textContent = formatDate(new Date());

            switch (json.weather[0].main.toLowerCase()) {
                case "clear":
                    image.src = "clear.png";
                    break;
                case "rain":
                    image.src = "rain.png";
                    break;
                case "clouds":
                    image.src = "cloud.png";
                    break;
                case "mist":
                    image.src = "mist.png";
                    break;
                case "haze":
                    image.src = "haze.png";
                    break;
                case "snow":
                    image.src = "snow.png";
                    break;
                default:
                    image.src = "cloud.png";
                    break;
            }
        })

        });


function displayError() {
    const image = document.querySelector(".weathercontainer img");
    const temp = document.querySelector(".weathercontainer .temp");
    const content = document.querySelector(".weathercontainer .content");
    const todayDate = document.querySelector(".weathercontainer .today");

    image.src = "errorpage.png"; 
    temp.innerHTML = '';
    content.textContent = `${document.querySelector(".searchcontainer input").value} not found`;
    todayDate.textContent = '';
}

function formatDate(date) {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    
    const dayName = days[date.getDay()];
    const monthName = months[date.getMonth()];
    const day = date.getDate();
    const year = date.getFullYear();

    return `${dayName}, ${day} ${monthName} ${year}`;
}
