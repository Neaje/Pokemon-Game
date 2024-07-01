<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Neaje/Pokemon-Game">
    <img src="assets/images/logo.png" alt="Logo" width="370" height="136">
  </a>

<h3 align="center">Pokémon Doge Game</h3>

 <p align="center">
    A relatively simple game involving the Pokémon universe.
 </p>
</div>


## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/Neaje/Pokemon-Game)

The objective of the game is straightforward : **to avoid capture by the Pokéballs.**

### Built With

* [![python][python]][python-url]
* [![python][pygame]][pygame-url]
* [![python][pyinstaller]][pyinstaller-url]

## Getting Started

There are multiple avenues for initiating the game, including the executable file or the Python script. The most simpliciter approach is to launch the executable directly. 

### Installation 
1. Clone the repo
```sh
git clone https://github.com/Neaje/Pokemon-Game && cd Pokemon-game
```
2. Install the python depencies 
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the python script and play
```sh 
python3 pokemon.py
```

Additionally, the executable can be constructed manually via the following command:
```sh
pyinstaller --onefile --windowed --add-data "assets/images:assets/images" script_v8.py

# The executable is now in the dist directory
dist
└── pokemon 
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[python]: https://img.shields.io/badge/python-0769AD?style=for-the-badge&logo=python
[pygame]: https://img.shields.io/badge/pygame-0769AD?style=for-the-badge&logo=python
[python-url]: https://www.python.org/
[pygame-url]: https://www.pygame.org/news
[pyinstaller]: https://img.shields.io/badge/pyinstaller-0769AD?style=for-the-badge&logo=python
[pyinstaller-url]: https://pypi.org/project/pyinstaller/
[product-screenshot]: assets/images/product-screenshot.png