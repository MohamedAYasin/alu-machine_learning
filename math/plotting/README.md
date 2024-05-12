# Resources

## Read or watch:

- [Plot (graphics)](https://intranet.aluswe.com/rltoken/swUAw_dV4-PhFth6wSzU1w)
- [Scatter plot](https://intranet.aluswe.com/rltoken/ukujmh-I_E6VTCLeJLiANw)
- [Line chart](https://intranet.aluswe.com/rltoken/gO3-Klt1z0tJeVU1aJD9qg)
- [Bar chart](https://intranet.aluswe.com/rltoken/JLN6oUJ6zbzZPW2i4Z_TaQ)
- [Histogram](https://intranet.aluswe.com/rltoken/FXDyUjw0H15E7AmmTo35LA)
- [Pyplot tutorial](https://intranet.aluswe.com/rltoken/Lq1HDu2VEMZi-yE_7ltscw)
- [matplotlib.pyplot](https://intranet.aluswe.com/rltoken/dLvKK7IoDp4iJ1SDOfXjbA)
- [matplotlib.pyplot.plot](https://intranet.aluswe.com/rltoken/xnkRJa0RUk11gHCn_4d7wg)
- [matplotlib.pyplot.scatter](https://intranet.aluswe.com/rltoken/G31zxaALPB8X6Tl0pGBKZg)
- [matplotlib.pyplot.bar](https://intranet.aluswe.com/rltoken/vWYnFhqY9BR2GcjwZeL93Q)
- [matplotlib.pyplot.hist](https://intranet.aluswe.com/rltoken/eK68OpXged-N3ln1JKx6uw)
- [matplotlib.pyplot.xlabel](https://intranet.aluswe.com/rltoken/thmt08lRjDru1ZveGf5K_A)
- [matplotlib.pyplot.ylabel](https://intranet.aluswe.com/rltoken/OVXA56hPedxzZQUsTsb3NQ)
- [matplotlib.pyplot.title](https://intranet.aluswe.com/rltoken/69jaiU_qxZXdmtw2H74V0w)
- [matplotlib.pyplot.subplot](https://intranet.aluswe.com/rltoken/tJyJnYmU379spf1PwDS5NA)
- [matplotlib.pyplot.subplots](https://intranet.aluswe.com/rltoken/hKc-OtsJ9jlFXFnpdw4rEA)
- [matplotlib.pyplot.subplot2grid](https://intranet.aluswe.com/rltoken/XlkmUFK2Q5etIUNXAfLl-A)
- [matplotlib.pyplot.suptitle](https://intranet.aluswe.com/rltoken/t45q5xSfiqFDoCsFTaQuhQ)
- [matplotlib.pyplot.xscale](https://intranet.aluswe.com/rltoken/DOhIVi9vhIx5PwVwX1YYLw)
- [matplotlib.pyplot.yscale](https://intranet.aluswe.com/rltoken/yPvF0-aSA20E-Ooa-Yi5XQ)
- [matplotlib.pyplot.xlim](https://intranet.aluswe.com/rltoken/ElRUPhxnBRJ04JjWyO1mJg)
- [matplotlib.pyplot.ylim](https://intranet.aluswe.com/rltoken/NqDCA5ih935PeOwUsdx3rw)
- [mplot3d tutorial](https://intranet.aluswe.com/rltoken/AYQjFMZVls_eLrJl7ELDbA)
- [additional tutorials](https://intranet.aluswe.com/rltoken/CUnX6P9AajVauF-4iDQORw)

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is a plot?
- What is a scatter plot? line graph? bar graph? histogram?
- What is matplotlib?
- How to plot data with matplotlib
- How to label a plot
- How to scale an axis
- How to plot multiple sets of data at the same time

# Requirements

## General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 16.04 LTS using python3 (version 3.5)
- Your files will be executed with numpy (version 1.15) and matplotlib (version 3.0)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Unless otherwise noted, you are not allowed to import any module
- All your files must be executable
- The length of your files will be tested using wc

# More Info

## Installing Matplotlib 3.0


To check that it has been successfully downloaded, use `pip list`.

## Configure X11 Forwarding

Update your Vagrantfile to include the following:

```plaintext
Vagrant.configure(2) do |config|
...
config.ssh.forward_x11 = true
end
