# Selenium Testing with ChromeDriver for Android devices and Behave


To get started, we'll need to install Phyton:  (pt/br -Para começar precisamos instalar Python)


[Installation documenation](https://www.python.org/downloads/) on the Python website 

### Behave. 
The easiest means of doing so is with Pip: (Behave - a maneira mais facil é executar o comando)

```
pip install Behave
```

[Installation documenation](http://pythonhosted.org/behave/install.html) on the Behave website.

### We also need to install Chromedriver (também precisamos instalar Chromedriver)

[Installation documenation](http://chromedriver.chromium.org/downloads) on the Chromedriver website.


Lastly, we'll need to install Selenium: (e por ultimo precisamos instalar o selenium).

```
pip install selenium
```

## Running a Test (Rodando o teste)

Once that's complete, you need to star your ChromeDriver Server (Depois da instalar você precisa dar start no seu sever)

1. Start the Android SDK's Android Debug Bridge (adb) server: (Ligue a ponte entre seu computador e o device)

```
$ adb start-server
```

2. Start the ChromeDriver server. It will print the port it is listening on: (Ligue o ChromeDriver server)
```
$ ./chromedriver
Started ChromeDriver (v2.0) on port 9515
```

connect or device and execute behave (Conecte seu device no pc e digite o comando.)

```
$ behave
```
