fetch("./qap5.json")
    .then((response) => response.json())
    .then((data) => {
        data.forEach((person) => {
            switch (person.id) {
                case "10":
                    console.log(`${person.name} is part of the management team`);
                    break;
                case "20":
                    console.log(`${person.name} is part of the sales team`);
                    break;
                case "30":
                    console.log(`${person.name} is part of the maintenance team`);
                    break;
                default:
                    console.log(`${person.name} may be due for promotion`);
            }
            console.log(person)
        });
    })
    .catch((error) => {
        console.error(error);
    });