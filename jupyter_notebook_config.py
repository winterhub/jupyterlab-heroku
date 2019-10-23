# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'sha1:b7141b3ba9f9:980cab33b65a92a408d07382ea4cd8a3b93235e8'
