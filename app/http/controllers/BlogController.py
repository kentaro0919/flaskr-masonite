""" A BlogController Module """
from masonite.view import View
from app.P

class BlogController:
    """Class Docstring Description
    """
    def __init__(self, view: View):
        self.view = view
        
        

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BlogController
        """

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BlogController
        """
        
        return self.view.render('index.html', {"posts"=posts})


    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", BlogController
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", BlogController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", BlogController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", BlogController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", BlogController)
        """

        pass