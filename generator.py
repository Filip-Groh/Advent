for i in range(1, 25):
    with open(f"{i}.html", mode="w", encoding="UTF-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Advent</title>
        <link rel="stylesheet" type="text/css" href="./stylesheet.css">
    </head>
    <body>
        <header>
            <h1>Advent</h1>
        </header>
        <nav>
            <a href="./index.html">
                <svg width="64px" height="64px" id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 122.88 113.97"><defs><style>.cls-1{"fill-rule:evenodd;"}</style></defs><title>homepage</title><path class="cls-1" d="M18.69,73.37,59.18,32.86c2.14-2.14,2.41-2.23,4.63,0l40.38,40.51V114h-30V86.55a3.38,3.38,0,0,0-3.37-3.37H52.08a3.38,3.38,0,0,0-3.37,3.37V114h-30V73.37ZM60.17.88,0,57.38l14.84,7.79,42.5-42.86c3.64-3.66,3.68-3.74,7.29-.16l43.41,43,14.84-7.79L62.62.79c-1.08-1-1.24-1.13-2.45.09Z"/></svg>
            </a>
            <menu>
                <li{" class='active'" if i == 1 else ""}><a href="./1.html">1</a></li>
                <li{" class='active'" if i == 2 else ""}><a href="./2.html">2</a></li>
                <li{" class='active'" if i == 3 else ""}><a href="./3.html">3</a></li>
                <li{" class='active'" if i == 4 else ""}><a href="./4.html">4</a></li>
                <li{" class='active'" if i == 5 else ""}><a href="./5.html">5</a></li>
                <li{" class='active'" if i == 6 else ""} id="mikulas"><a href="./6.html">6</a></li>
                <li{" class='active'" if i == 7 else ""}><a href="./7.html">7</a></li>
                <li{" class='active'" if i == 8 else ""}><a href="./8.html">8</a></li>
                <li{" class='active'" if i == 9 else ""}><a href="./9.html">9</a></li>
                <li{" class='active'" if i == 10 else ""}><a href="./10.html">10</a></li>
                <li{" class='active'" if i == 11 else ""}><a href="./11.html">11</a></li>
                <li{" class='active'" if i == 12 else ""}><a href="./12.html">12</a></li>
                <li{" class='active'" if i == 13 else ""}><a href="./13.html">13</a></li>
                <li{" class='active'" if i == 14 else ""}><a href="./14.html">14</a></li>
                <li{" class='active'" if i == 15 else ""}><a href="./15.html">15</a></li>
                <li{" class='active'" if i == 16 else ""}><a href="./16.html">16</a></li>
                <li{" class='active'" if i == 17 else ""}><a href="./17.html">17</a></li>
                <li{" class='active'" if i == 18 else ""}><a href="./18.html">18</a></li>
                <li{" class='active'" if i == 19 else ""}><a href="./19.html">19</a></li>
                <li{" class='active'" if i == 20 else ""}><a href="./20.html">20</a></li>
                <li{" class='active'" if i == 21 else ""}><a href="./21.html">21</a></li>
                <li{" class='active'" if i == 22 else ""}><a href="./22.html">22</a></li>
                <li{" class='active'" if i == 23 else ""}><a href="./23.html">23</a></li>
                <li{" class='active'" if i == 24 else ""} id="vanoce"><a href="./24.html">24</a></li>
            </menu>
        </nav>
        <article>
            <section>
                <h2>{i}</h2>
            </section>
            <section class="squeeze">
                <h2>Obrázek:</h2>
                <img src="./src/{i}.jfif" alt="Advent Image">
                {"<p>Vánoce!!!!!!!!!!!!!!!!!!!</p>" if i == 24 else ""}
            </section>
        </article>
        <footer>
            Filip Groh ©copyright 2023
        </footer>
    </body>
</html>        
        """)