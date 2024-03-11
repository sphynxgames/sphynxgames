# Let's create a Python script that generates HTML files for each game with the specified details.

games_info = {
    'Stacktris': 'https://boxing2.github.io/b6/stacktris/',
    'MonkeyMart': 'https://monkeymartgame.github.io/file/',
    '1v1LOL': 'https://purepro4561.github.io/1v1-Lol/',
    'BloonsTD4': 'https://www.bubbleshooter.net/embed.php?id=655',
}

# Base HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{game_name} - Sphynx Games</title>
    <link rel="stylesheet" href="../style.css">
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const fullscreenBtn = document.getElementById('fullscreenBtn');
            const header = document.querySelector('header');
            const footer = document.querySelector('footer');
            const gameIframe = document.getElementById('gameIframe');
            const body = document.body;
        
            fullscreenBtn.addEventListener('click', function() {{
                let isFullscreen = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement;
        
                if (!isFullscreen) {{ // Enter fullscreen
                    if (document.documentElement.requestFullscreen) {{
                        document.documentElement.requestFullscreen();
                    }} else if (document.documentElement.webkitRequestFullscreen) {{
                        document.documentElement.webkitRequestFullscreen();
                    }} else if (document.documentElement.mozRequestFullScreen) {{
                        document.documentElement.mozRequestFullScreen();
                    }} else if (document.documentElement.msRequestFullscreen) {{
                        document.documentElement.msRequestFullscreen();
                    }}
                    gameIframe.style.width = '100vw';
                    gameIframe.style.height = '100vh';
                    gameIframe.style.borderRadius = '0';
                    gameIframe.style.zIndex = '2147483647'; // Max z-index value to ensure it's on top
                    header.style.display = 'none'; // Hide the header
                    footer.style.display = 'none'; // Hide the footer
                    fullscreenBtn.style.display = 'none'; // Hide the fullscreen button
                    body.style.overflow = 'hidden'; // Prevent scrolling
                    gameIframe.focus(); // Focus on the iframe
                }}
            }});
        
            document.addEventListener('fullscreenchange', exitHandler);
            document.addEventListener('webkitfullscreenchange', exitHandler);
            document.addEventListener('mozfullscreenchange', exitHandler);
            document.addEventListener('MSFullscreenChange', exitHandler);
        
            function exitHandler() {{
                if (!document.fullscreenElement && !document.webkitIsFullScreen && !document.mozFullScreen && !document.msFullscreenElement) {{
                    // Exited fullscreen mode, revert changes
                    gameIframe.style.width = '640px';
                    gameIframe.style.height = '480px';
                    gameIframe.style.borderRadius = '10px';
                    gameIframe.style.zIndex = 'auto'; // Reset z-index
                    header.style.display = 'flex'; // Show the header again
                    footer.style.display = 'block'; // Show the footer again
                    fullscreenBtn.style.display = 'block'; // Show the fullscreen button again
                    body.style.overflow = 'auto'; // Allow scrolling
                }}
            }}
        
            function exitFullscreen() {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }} else if (document.webkitExitFullscreen) {{
                    document.webkitExitFullscreen();
                }} else if (document.mozCancelFullScreen) {{
                    document.mozCancelFullScreen();
                }} else if (document.msExitFullscreen) {{
                    document.msExitFullscreen();
                }}
            }}
        }});
    </script>
    <style>
        .game-iframe-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        iframe#gameIframe {{
            width: 640px; /* Adjust the width as needed */
            height: 480px; /* Adjust the height as needed */
            border-radius: 10px; /* Adds rounded corners to the iframe */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Adds a drop shadow for depth */
        }}
        button {{
            display: block;
            margin: 20px auto; /* Centers the button below the iframe */
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo-container">
            <img src="../Assets/Logo.png" alt="Sphynx Games Logo">
        </div>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../about.html">About Us</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <div class="game-iframe-container">
            <iframe id="gameIframe" src="https://api.codetabs.com/v1/proxy/?quest={embed_url}" frameborder="0"></iframe>
            <button id="fullscreenBtn">Go Fullscreen</button>
        </div>    
    </main>
    <footer>
        <p>&copy; 2024 Sphynx Games. All rights reserved.</p>
    </footer>
</body>
</html>
"""

for game_name, embed_url in games_info.items():
    file_name = f"{game_name}.html"
    html_content = html_template.format(game_name=game_name.replace(' ', ''), embed_url=embed_url)
    with open(file_name, 'w') as file:
        file.write(html_content)
# Original last line: "HTML files created successfully."
print("HTML files created successfully. Press Enter to exit...")
input()  # Wait for user input before closing

