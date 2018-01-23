import timeit

dot_product_1000_to_1000="""

l1 = np.random.random_integers(0, 1, (1000, ))
connections = np.random.random_integers(0,1, (1000, 1000))
l2 = np.dot(connections, l1)

"""

dot_product_5000_to_5000="""

l1 = np.random.random_integers(0, 1, (5000, ))
connections = np.random.random_integers(0,1, (5000, 5000))
l2 = np.dot(connections, l1)

"""

dot_product_10000_to_10000="""

l1 = np.random.random_integers(0, 1, (10000, ))
connections = np.random.random_integers(0,1, (10000, 10000))
l2 = np.dot(connections, l1)

"""

dot_product_100000_to_100000="""

l1 = np.random.randint(0, 1, (100000, ),dtype='int8')
connections = np.random.randint(0,1, (100000, 100000), dtype='int8')
l2 = np.dot(connections, l1)

"""

thousand = (timeit.timeit(dot_product_1000_to_1000, number=3, setup="import numpy as np"))
five_t= (timeit.timeit(dot_product_5000_to_5000, number=3, setup="import numpy as np"))
ten_t = (timeit.timeit(dot_product_10000_to_10000, number=3, setup="import numpy as np"))
hundred_t = (timeit.timeit(dot_product_100000_to_100000, number=2, setup="import numpy as np"))


report = """
<html>
<body>
<div>
<h2>Performance Test:</h2>

<h3>-------1--------</h3>

<strong>Number of layers:</strong> 2 <br/>
<strong>No. of neurons in layer 1:</strong> 1000 <br/>
<strong>No. of neurons in layer 2:</strong> 1000 <br/>
<strong>Connections:</strong> Fully connected ([1000,1000] connection matrix) <br/>
<strong>Operation:</strong> Calculate total input to Layer 2 neurons from Layer 1 by 
multiplying Layer 1 neurons with appropriate connections (dot product) <br/>
<strong>Time taken in seconds(best from three tries):</strong> {} <br/>
<br/><br/>

<h3>----------2------------</h3>

<strong>Number of layers:</strong> 2 <br/>
<strong>No. of neurons in layer 1:</strong> 5000 <br/>
<strong>No. of neurons in layer 2:</strong> 5000 <br/>
<strong>Connections:</strong> Fully connected ([5000,5000] connection matrix) <br/>
<strong>Operation:</strong> Calculate total input to Layer 2 neurons from Layer 1 by 
multiplying Layer 1 neurons with appropriate connections (dot product) <br/>
<strong>Time taken in seconds(best from three tries):</strong> {} <br/>
<br/><br/>


<h3>----------------------3------------</h3>

<strong>Number of layers:</strong> 2 <br/>
<strong>No. of neurons in layer 1:</strong> 1000 <br/>
<strong>No. of neurons in layer 2:</strong> 1000 <br/>
<strong>Connections:</strong> Fully connected ([1000,1000] connection matrix) <br/>
<strong>Operation:</strong> Calculate total input to Layer 2 neurons from Layer 1 by 
multiplying Layer 1 neurons with appropriate connections (dot product) <br/>
<strong>Time taken in seconds(best from three tries):</strong> {} <br/>
<br/><br/>

<h3>----------------4-----------------------</h3>

<strong>Number of layers:</strong> 2 <br/>
<strong>No. of neurons in layer 1:</strong> 100000 <br/>
<strong>No. of neurons in layer 2:</strong> 100000 <br/>
<strong>Connections:</strong> Fully connected (<strong>[100000,100000] connection matrix</strong>) <br/>
<strong>Operation:</strong> Calculate total input to Layer 2 neurons from Layer 1 by 
multiplying Layer 1 neurons with appropriate connections (dot product) <br/>
<strong>Time taken in seconds(best from three tries):</strong> {} <br/>
<br/><br/>

</div>
</body>
</html>
""".format(thousand, five_t, ten_t, hundred_t)


from app.report.mailer import send_mail

send_mail('reports@mail.cyces.co', (
        'kandhan.kuhan@gmail.com',
        'ananthakumar.akr@gmail.com',
        'thecorptechteam@gmail.com',
        'vidushi.meenu@gmail.com',
        'rootat1306@gmail.com',
    ), subject='Performance test on Monster Machine #2', message=report)