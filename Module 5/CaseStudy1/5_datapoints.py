import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = [20, 21, 20.5, 20.8]
    # 1. simple plot
    plt.plot(x,y)
    plt.show()

    # 2. line and marker style in simple plot
    plt.grid()
    plt.plot(x,y,'-.')
    plt.plot(x,y,'o')
    plt.show()

    # 3. configure the axes
    plt.plot(x,y)
    plt.axis([1,5,15,25])
    plt.show()

    # 4. Give title of Graph & labels of x axis and y axis
    plt.plot(x,y)
    plt.xlabel('X- axis')
    plt.ylabel('Y-axis')
    plt.title('X-axis vs Y-axis')
    plt.legend()
    plt.show()

    # 5. Give error bar if
    y_error = [0.12, 0.13, 0.2, 0.1]
    plt.plot(x,y,y_error)
    plt.xlabel('X- axis')
    plt.ylabel('Y-axis')
    plt.title('graph with error bar ')
    plt.show()

    # 6. define width, height as figsize=(4,5) DPI and adjust plot dpi=100
    plt.figure(figsize=(4, 5), dpi=100)
    plt.plot(x,y)
    plt.show()

    # 7. Give a font size of 14
    plt.plot(x,y)
    plt.rcParams.update({'font.size': 14})  #runtime configuration params - rcparams
    plt.show()

    # 8. Draw a scatter graph of any 50 random values of x and y axis
    a = np.random.randn(50)
    b = np.random.randn(50)
    plt.scatter(a,b)
    plt.show()

    # 9. Create a dataframe from following data
    dataframe = pd.DataFrame({
        'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3], 'postTestScore': [25, 94, 57, 62, 70]
    })
    ax = dataframe['preTestScore']
    ay = dataframe['postTestScore']
    size = dataframe['age']
    plt.xlabel('preTestScore')
    plt.ylabel('postTestScore')
    plt.title('scatter plot with size of each point by age ')
    plt.scatter(ax,ay,s=size)
    plt.show()

    # 10. preTestScore and postTestScore with the size = 300 and the color determined by sex
    dataframe = pd.DataFrame({
        'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3], 'postTestScore': [25, 94, 57, 62, 70]
    })
    ax = dataframe['preTestScore']
    ay = dataframe['postTestScore']
    color = dataframe['female']
    plt.xlabel('preTestScore')
    plt.ylabel('postTestScore')
    plt.title('scatter plot with size 300 and color of each point by sex ')
    plt.scatter(ax,ay,s=300,c=color)
    plt.show()