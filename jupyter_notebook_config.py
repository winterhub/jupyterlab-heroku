# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha256:845f42336140:7ffc4772aa77f51815bbb4ea08919bfd7be305907e1d82d5645abc1512151654'
