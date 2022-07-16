links = ['Home', 'About', 'Contact'];




function Nav(links) {
    return (
        `<nav class="container">
        <ul class="tabs is-right">
            ${links.map(({ name }) => (`
            <li key=\"${name}\" class="navbar-brand">
                <a href=/\"${name}\" class="navbar-item is-active is-size-5 has-text-weight-semibold">
                ${name}
                </a>
            </li>
           `))}
        </ul>
        </nav>`

    ).split(",") .join("");
    }
    