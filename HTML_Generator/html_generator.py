import tkinter as tk
import tkinter.filedialog as filedialog


class HtmlGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("HTML Generator")
        # Minimum size of application window
        self.master.minsize(800, 800)

        # Maximum size of application window
        self.master.maxsize(1024, 1024)

        self.master.configure(background="#33261D")

        # Create the header frame
        self.header_frame = tk.Frame(self.master, bg="#334E58", height=200)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        # Initialize the list of boxes
        self.boxes = []

        # Dictionary to contain box IDs
        self.box_ids = {}

        # Initialize the list of subsection title
        self.subsection_title = []

        # Initialize the list of subsection body
        self.subsection_body = []

        # Dictionary to contain subsection IDs
        self.subsection_ids = {}

        # Create the left box in the header
        self.left_box_id = self.generate_id()
        self.left_box = tk.Entry(self.header_frame, bg="white", fg="black", width=20, relief=tk.RIDGE)
        self.left_box.pack(side=tk.LEFT, padx=10, pady=20)
        self.left_box.bind("<FocusIn>", self.focus_in)
        self.left_box.bind("<FocusOut>", self.focus_out)
        self.left_box.insert(0, "image url")
        self.boxes.append(self.left_box)

        # Create the add button in the header
        self.add_button = tk.Button(self.header_frame, text="Add Menu", command=self.add_box)
        self.add_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Create the box count variable
        self.box_count = 1

        # Create the body frame
        self.body_frame = tk.Frame(self.master, bg="#FCBFB7")
        self.body_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Entry widget for website title
        self.website_title = tk.Entry(self.body_frame, bg="white", fg="black", width=50, relief=tk.RIDGE)
        self.website_title.pack(side=tk.TOP, padx=10, pady=20, anchor='w')
        self.website_title.insert(0, "Website title")

        # Entry widget for website H1 heading
        self.h1_heading = tk.Entry(self.body_frame, bg="white", fg="black", width=50, relief=tk.RIDGE)
        self.h1_heading.pack(side=tk.TOP, padx=10, pady=20, anchor='w')
        self.h1_heading.insert(0, "Main H1 Heading")

        # Text widget for website main description
        self.main_description = tk.Entry(self.body_frame, bg="white", fg="black", width=100, relief=tk.RIDGE)
        self.main_description.pack(side=tk.TOP, padx=10, pady=20, anchor='w')
        self.main_description.insert(tk.END, "Main description")

        # Create the generate button
        self.add_subsection = tk.Button(self.body_frame, text="Add Sub Section", command=self.add_subsection)
        self.add_subsection.pack(side=tk.TOP, padx=10, pady=10)

        # Create the generate button
        self.generate_button = tk.Button(self.master, text="Generate HTML", command=self.generate_html)
        self.generate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def generate_id(self):
        return len(self.boxes) + 1

    def focus_in(self, event):
        if event.widget == self.left_box:
            if self.left_box.get() == f"Box {self.left_box_id}":
                self.left_box.delete(0, tk.END)

    def focus_out(self, event):
        if event.widget == self.left_box:
            if self.left_box.get() == "":
                self.left_box.insert(0, f"Box {self.left_box_id}")
            else:
                #  self.boxes[self.boxes.index(self.left_box)]["id"] = self.left_box.get()
                self.box_ids[self.boxes.index(self.left_box)] = self.left_box.get()

    def add_box(self):
        # Check if the maximum number of boxes has been reached
        if self.box_count >= 4:
            self.add_button.configure(text="Max Reached")
            return

        # Create a new box text box
        new_box_id = self.generate_id()
        new_box = tk.Entry(self.header_frame, bg="white", fg="black", width=20, relief=tk.RIDGE)
        new_box.pack(side=tk.LEFT, padx=10, pady=5)
        new_box.bind("<FocusIn>", self.focus_in)
        new_box.bind("<FocusOut>", self.focus_out)
        new_box.insert(0, f"Box {new_box_id}")

        # Pack the new box text box to the left of the add button
        self.add_button.pack_forget()
        new_box.pack(side=tk.LEFT, padx=10, pady=5)
        self.add_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Add the new box text box to the list of boxes
        self.boxes.append(new_box)

        # Increment the box count
        self.box_count += 1

    def add_subsection(self):
        # Create subsection heading
        new_subsection_id = self.generate_id()
        new_title = tk.Entry(self.body_frame, bg="white", fg="black", width=20, relief=tk.RIDGE)
        new_title.pack(side=tk.TOP, padx=10, pady=5)
        new_title.insert(0, "Sub section heading")

        # Create subsection body
        new_body = tk.Entry(self.body_frame, bg="white", fg="black", width=40, relief=tk.RIDGE)
        new_body.pack(side=tk.TOP, padx=10, pady=5)
        new_body.insert(0, "Sub section body")



        # Add the new subsection title to the list of titles
        self.subsection_title.append(new_title)

        # Add the new subsection body to the list of subsection bodies
        self.subsection_body.append(new_body)


    def generate_html(self):
        # Get the image URL from the left box
        image_url = self.left_box.get()

        # get the website title
        website_title = self.website_title.get()

        # Get the menu items from the other boxes
        menu_items = [box.get() for box in self.boxes[1:]]

        sub_title = [subsection.get() for subsection in self.subsection_title]
        sub_body = [sub_sec_body.get() for sub_sec_body in self.subsection_body]

        # Generate the HTML code for subsections
        subsection_html = [f"<h2>{sub_title[i]}</h2><p>{sub_body[i]}</p>" for i in range(len(sub_title))]
        subsection_html = "".join(subsection_html)

        # Generate the HTML code
        html_code = f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>{website_title}</title>
                    <style>
    body {{
        margin-left: auto;
        margin-right: auto;
    }}

    header {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #f0f0f0;
        height: 80px;
        max-width: 100%;
    }}

    img {{
        height: 60px;
        margin-left: 20px;
    }}

    ul {{
        list-style: none;
        display: flex;
        margin-right: 20px;
    }}

    li {{
        margin-left: 20px;
    }}

    a {{
        text-decoration: none;
        color: #333;
        font-size: 18px;
    }}

    main {{
        margin: 0 auto;
        max-width: 800px;
    }}

    .main-description {{
        margin: 20px;
    }}

    .main-description h2 {{
        font-size: 24px;
        margin-bottom: 10px;
    }}

    .main-description p {{
        font-size: 18px;
        line-height: 1.5;
    }}
</style>
                </head>
                <body>
                    <header>
                        <img src="{image_url}" alt="Logo">
                        <nav>
                            <ul>
                                {"".join([f"<li>{item}</li>" for item in menu_items])}
                            </ul>
                        </nav>
                    </header>
                    <main>
                        <h1>{self.h1_heading.get()}</h1>
                        <p>{self.main_description.get()}</p>
                        <div class="main-description">
                            {subsection_html}
                        </div>
                    </main>
                </body>
            </html>
        """

        # Save the HTML code to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".html")
        if file_path:
            with open(file_path, "w") as html_file:
                html_file.write(html_code)


if __name__ == "__main__":
    root = tk.Tk()
    app = HtmlGenerator(root)
    root.mainloop()
