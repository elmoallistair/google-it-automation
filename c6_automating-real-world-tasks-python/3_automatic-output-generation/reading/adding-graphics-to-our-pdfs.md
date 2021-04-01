## Adding Graphics to our PDFs

Up to now, we've generated a report with a title and a table of data. Next let's add something a little more graphical. What could be better than a fruit pie (graph)?! We’re going to need to use the ***Drawing*** Flowable class to create a ***Pie*** chart.

```
>>> from reportlab.graphics.shapes import Drawing
>>> from reportlab.graphics.charts.piecharts import Pie
>>> report_pie = Pie(width=3*inch, height=3*inch)
```

To add data to our **Pie** chart, we need two separate lists: One for data, and one for labels. Once more, we’re going to have to transform our fruit dictionary into a different shape. For an added twist, let's sort the fruit in alphabetical order:

```
>>> report_pie.data = []
>>> report_pie.labels = []
>>> for fruit_name in sorted(fruit):
...   report_pie.data.append(fruit[fruit_name])
...   report_pie.labels.append(fruit_name)
...
>>> print(report_pie.data)
[2, 5, 8, 3, 1, 1, 13]
>>> print(report_pie.labels)
['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']
```

The **Pie** object isn’t Flowable, but it can be placed inside of a Flowable ***Drawing***.

```
>>> report_chart = Drawing()
>>> report_chart.add(report_pie)
```

Now, we'll add the new Drawing to the report, and see what it looks like.

```
report.build([report_title, report_table, report_chart])
```

![img](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/kB8L5tDnR_qfC-bQ5xf6MQ_fedb9ca05eec18eb64a7f541e5b855c9_pasted-image-0-3-.png?expiry=1597276800000&hmac=dfptvvOO7Cu23S5NxGeBg0cVIP7ZWjABeu3AEX0ViPo)

Alright, and with that, you've seen a few examples of what we can do with the ReportLab library.  There's a ton more things that can be done that we won't cover here. You'll want to refer to the [ReportLab User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf) for more details on the features we've seen, and to see what else you can create with it.

By the way, the ReportLab User Guide is a PDF that [is generated using reportlab](https://bitbucket.org/rptlab/reportlab/src/default/docs/)! Cool, right?