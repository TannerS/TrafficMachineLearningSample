## Prompt

"< road id, direction, dayOfWeek, timeOfDay >  => < traffic status >"

"<10, 0, 1, 8> => <8>"    // for I-10 west, Monday at 8am, the traffic is 8 (1-10)

"<10, 0, 2, 9> => <7>"

"<10, 1, 1, 13> => <5>"

"<5, 0, 1, 15> => <6>"

"<5, 1, 5, 16> => <9>"    // for I-5 south, Friday at 4pm, the traffic is 9

"<5, 1, 6, 18> => <9>"


## The machine learning algorithm 

Polynomial interpolation

## Model

Ridge Regression

`model = make_pipeline(PolynomialFeatures(2), Ridge())`

This meansthis model will use a line based on a degree 2 polynomial 
