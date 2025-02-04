import React from 'react';
import './About.css';


function About(props) {
    const [theme,setTheme] = React.useState('dark');

    const toggleTheme = () => (
        setTheme(theme==="light"?"dark":"light")
    );
    return (
        <div className={theme} id="about">
            {/* Add the button element here */}
            <button  id="about-button"className={theme === "dark" ? "dark" : "light"}
                    onClick={toggleTheme}>{theme === "light" ? "Dark" : "Light"} theme
            </button>
            <h2>Why We Explore - NASA</h2>

            <p id="para">
                Humans are driven to explore the unknown, discover new worlds, push
                the boundaries of our scientific and technical limits, and then push
                further. The intangible desire to explore and challenge the boundaries
                of what we know and where we have been has provided benefits to our
                society for centuries.
            </p>
        </div>
    );
}

export default About;