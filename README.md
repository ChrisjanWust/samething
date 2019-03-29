# samething
Python module indicating whether two strings refer to the same thing by returning a confidence score.

## Module layout

![Samething diagram](https://github.com/slvrcld/samething/blob/master/diagram.png?raw=true)

( Diagram can be edited here: https://drive.google.com/file/d/1UVSwytgSTih4w3Em_3yR6W3FwSP41VDv/view?usp=sharing )


## Usage
2 external modules are required, but both are standard: `re` and `operator`.

Running `testing.py` should give the following output:

```
  [
    {'index': 46, 'name': 'Samsung Galaxy S5', 'confidence': 0.9227527113617434},
    {'index': 42, 'name': 'Samsung Galaxy S5 Plus', 'confidence': 0.8674178833024107},
    {'index': 43, 'name': 'Samsung Galaxy S5 Neo', 'confidence': 0.8674178833024107},
    {'index': 47, 'name': 'Samsung Galaxy S5 (USA)', 'confidence': 0.8674178833024107},
    {'index': 48, 'name': 'Samsung Galaxy S5 Duos', 'confidence': 0.8674178833024107},
    {'index': 49, 'name': 'Samsung Galaxy S5 (octa-core)', 'confidence': 0.8674178833024107},
    {'index': 50, 'name': 'Samsung Galaxy S5 Active', 'confidence': 0.8674178833024107},
    {'index': 52, 'name': 'Samsung Galaxy S5 Sport', 'confidence': 0.8674178833024107},
    {'index': 53, 'name': 'Samsung Galaxy S5 mini', 'confidence': 0.8674178833024107},
    {'index': 54, 'name': 'Samsung Galaxy S5 mini Duos', 'confidence': 0.8252981176259454},
    ...
  ]
```

