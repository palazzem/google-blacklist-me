Google blacklist me
===================

*(aka "Scrape some emails around using Google search")*

**DISCLAIMER**: this is a code example for Scrapy_. **DON'T USE IT** for bad purpose or for your production
environment.

This code is used during `PyConIT talk`_: "From website to JSON data in 30 minutes with Scrapy".

How to use it
-------------

.. code-block::

    $ pip install -r requirements.txt

Create ``urls.txt`` file and put Google search keyword for each lines like

.. code-block::

    PyCon
    Evonove
    Wow

Launch your scraper with

.. code-block::

    $ scrapy crawl bot -a filename=urls.txt -o emails.json -t json

Happy email crawling!

.. _Scrapy: http://scrapy.org/
.. _PyConIT talk: https://www.pycon.it/conference/talks/da-sito-web-a-dati-json-in-30-minuti-con-scrapy
