import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt

from auth import Authentication
from donation_manager import DonationManager
from recipient_manager import recipient_manager
from priority import PriorityManager
from data_analysis import DataAnalyzer


class DonEatGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "DonEat - Smart Food Donation & Food Rescue System"
        )

        self.root.geometry("1250x750")
        self.root.minsize(1050, 650)


        # COLORS


        self.dark_green = "#064E3B"
        self.green = "#0F766E"
        self.light_green = "#D1FAE5"

        self.white = "#FFFFFF"
        self.background = "#F5F7F6"

        self.blue = "#DBEAFE"
        self.red = "#FEE2E2"
        self.yellow = "#FEF3C7"
        self.purple = "#EDE9FE"

        self.text_dark = "#12372A"
        self.text_gray = "#64748B"

        # Palette used for charts (food types, priority, status, etc.)
        self.chart_palette = [
            "#0F766E",
            "#F59E0B",
            "#EF4444",
            "#3B82F6",
            "#8B5CF6",
            "#EC4899",
            "#10B981",
            "#F97316",
            "#6366F1",
            "#14B8A6"
        ]


        # PROJECT CLASSES


        self.auth = Authentication()
        self.donation_manager = DonationManager()
        self.recipient_manager = recipient_manager()
        self.priority_manager = PriorityManager()
        self.analyzer = DataAnalyzer()

        self.current_user = None

        self.setup_style()

        self.login_screen()


    # STYLE


    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            background="white",
            foreground=self.text_dark,
            rowheight=38,
            fieldbackground="white",
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            background=self.dark_green,
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=8
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#A7F3D0")
            ],
            foreground=[
                ("selected", self.text_dark)
            ]
        )

        style.configure(
            "TButton",
            font=("Arial", 10, "bold"),
            padding=8
        )


    # CLEAR SCREEN


    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # LOGIN


    def login_screen(self):

        self.clear_screen()

        self.root.configure(
            bg=self.dark_green
        )

        # Main container

        container = tk.Frame(
            self.root,
            bg=self.dark_green
        )

        container.pack(
            fill="both",
            expand=True
        )


        # LEFT SIDE


        left = tk.Frame(
            container,
            bg=self.dark_green,
            width=500
        )

        left.pack(
            side="left",
            fill="both",
            expand=True
        )

        left.pack_propagate(False)

        tk.Label(
            left,
            text="🍽️",
            font=("Arial", 70),
            bg=self.dark_green,
            fg="white"
        ).pack(
            pady=(100, 10)
        )

        tk.Label(
            left,
            text="DonEat",
            font=("Arial", 38, "bold"),
            bg=self.dark_green,
            fg="white"
        ).pack()

        tk.Label(
            left,
            text="Smart Food Donation\n& Food Rescue System",
            font=("Arial", 16),
            bg=self.dark_green,
            fg="#D1FAE5",
            justify="center"
        ).pack(
            pady=15
        )

        tk.Label(
            left,
            text="🥕  🍎  🥖  🥛  🥦",
            font=("Arial", 28),
            bg=self.dark_green,
            fg="white"
        ).pack(
            pady=20
        )

        tk.Label(
            left,
            text="Save Food • Help People • Reduce Waste",
            font=("Arial", 11),
            bg=self.dark_green,
            fg="white"
        ).pack()


        # RIGHT SIDE


        right = tk.Frame(
            container,
            bg=self.background
        )

        right.pack(
            side="right",
            fill="both",
            expand=True
        )

        card = tk.Frame(
            right,
            bg="white"
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.75,
            relheight=0.75
        )

        tk.Label(
            card,
            text="Welcome Back 👋",
            font=("Arial", 25, "bold"),
            bg="white",
            fg=self.text_dark
        ).pack(
            pady=(50, 5)
        )

        tk.Label(
            card,
            text="Login to your DonEat account",
            font=("Arial", 11),
            bg="white",
            fg=self.text_gray
        ).pack(
            pady=(0, 30)
        )

        tk.Label(
            card,
            text="Email",
            font=("Arial", 10, "bold"),
            bg="white",
            fg=self.text_dark
        ).pack(
            anchor="w",
            padx=45
        )

        self.email_entry = tk.Entry(
            card,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.email_entry.pack(
            fill="x",
            padx=45,
            pady=(5, 15),
            ipady=8
        )

        tk.Label(
            card,
            text="Password",
            font=("Arial", 10, "bold"),
            bg="white",
            fg=self.text_dark
        ).pack(
            anchor="w",
            padx=45
        )

        self.password_entry = tk.Entry(
            card,
            show="*",
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.password_entry.pack(
            fill="x",
            padx=45,
            pady=(5, 20),
            ipady=8
        )

        tk.Button(
            card,
            text="LOGIN",
            command=self.login,
            bg=self.green,
            fg="white",
            activebackground=self.dark_green,
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            fill="x",
            padx=45,
            pady=5,
            ipady=8
        )

        tk.Button(
            card,
            text="Create New Account",
            command=self.register_screen,
            bg="white",
            fg=self.green,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(
            pady=15
        )


    # LOGIN FUNCTION


    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get()

        if not email or not password:

            messagebox.showerror(
                "Error",
                "Please enter email and password."
            )

            return

        users = self.auth.load_users()

        for user_id, user in users.items():

            if user.get("Email") == email:

                if user.get("Password") == password:

                    self.current_user = user

                    self.dashboard()

                    return

                else:

                    messagebox.showerror(
                        "Error",
                        "Incorrect password."
                    )

                    return

        messagebox.showerror(
            "Error",
            "Email is not registered."
        )


    # REGISTER


    def register_screen(self):

        self.clear_screen()

        self.root.configure(
            bg=self.background
        )

        frame = tk.Frame(
            self.root,
            bg="white"
        )

        frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relwidth=0.55,
            relheight=0.85
        )

        tk.Label(
            frame,
            text="🍽️ Create DonEat Account",
            font=("Arial", 25, "bold"),
            bg="white",
            fg=self.text_dark
        ).pack(
            pady=25
        )

        self.register_entries = {}

        fields = [
            "Name",
            "Email",
            "Phone",
            "Password"
        ]

        for field in fields:

            tk.Label(
                frame,
                text=field,
                font=("Arial", 10, "bold"),
                bg="white",
                fg=self.text_dark
            ).pack(
                anchor="w",
                padx=50,
                pady=(5, 2)
            )

            entry = tk.Entry(
                frame,
                font=("Arial", 10),
                show="*" if field == "Password" else ""
            )

            entry.pack(
                fill="x",
                padx=50,
                ipady=5
            )

            self.register_entries[field] = entry

        tk.Label(
            frame,
            text="Role",
            font=("Arial", 10, "bold"),
            bg="white"
        ).pack(
            anchor="w",
            padx=50,
            pady=(10, 2)
        )

        self.role_var = tk.StringVar(
            value="donor"
        )

        role_box = ttk.Combobox(
            frame,
            textvariable=self.role_var,
            values=[
                "donor",
                "receiver",
                "volunteer"
            ],
            state="readonly"
        )

        role_box.pack(
            fill="x",
            padx=50
        )

        tk.Button(
            frame,
            text="CREATE ACCOUNT",
            command=self.register_user,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(
            fill="x",
            padx=50,
            pady=20,
            ipady=8
        )

        tk.Button(
            frame,
            text="Back to Login",
            command=self.login_screen,
            bg="white",
            fg=self.green,
            relief="flat"
        ).pack()


    # REGISTER USER


    def register_user(self):

        name = self.register_entries["Name"].get().strip()
        email = self.register_entries["Email"].get().strip()
        phone = self.register_entries["Phone"].get().strip()
        password = self.register_entries["Password"].get()

        role = self.role_var.get()

        if not name or not email or not phone or not password:

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        if len(password) != 8:

            messagebox.showerror(
                "Error",
                "Password must contain exactly 8 characters."
            )

            return

        chars = "!|$%^&*#.><?-_+{}[])(@~"

        if not any(
            char in password
            for char in chars
        ):

            messagebox.showerror(
                "Error",
                "Password must contain a special character."
            )

            return

        users = self.auth.load_users()

        new_id = self.auth.generate_id(
            users
        )

        new_user = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Password": password,
            "Role": role
        }

        if role in [
            "donor",
            "receiver"
        ]:

            new_user[
                "Organization name"
            ] = ""

            new_user[
                "Organization address"
            ] = ""

        else:

            new_user[
                "Availability"
            ] = ""

        users[new_id] = new_user

        self.auth.save_users(
            users
        )

        messagebox.showinfo(
            "Success",
            "Account created successfully!"
        )

        self.login_screen()


    # DASHBOARD


    def dashboard(self):

        self.clear_screen()

        self.root.configure(
            bg=self.background
        )


        # SIDEBAR


        self.sidebar = tk.Frame(
            self.root,
            bg=self.dark_green,
            width=240
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # Logo

        tk.Label(
            self.sidebar,
            text="🍽️",
            font=("Arial", 35),
            bg=self.dark_green,
            fg="white"
        ).pack(
            pady=(25, 0)
        )

        tk.Label(
            self.sidebar,
            text="DonEat",
            font=("Arial", 24, "bold"),
            bg=self.dark_green,
            fg="white"
        ).pack()

        tk.Label(
            self.sidebar,
            text="Smart Food Rescue",
            font=("Arial", 9),
            bg=self.dark_green,
            fg="#A7F3D0"
        ).pack(
            pady=(0, 25)
        )

        # Menu

        menu = [
            ("🏠   Dashboard", self.home_page),
            ("🍱   Donations", self.donations_page),
            ("👥   Requests", self.requests_page),
            ("⭐   Smart Priority", self.priority_page),
            ("📊   Analytics", self.analytics_page)
        ]

        for text, command in menu:

            tk.Button(
                self.sidebar,
                text=text,
                command=command,
                bg=self.dark_green,
                fg="white",
                activebackground=self.green,
                activeforeground="white",
                font=("Arial", 11, "bold"),
                relief="flat",
                anchor="w",
                padx=20,
                cursor="hand2"
            ).pack(
                fill="x",
                padx=10,
                pady=3,
                ipady=10
            )

        # Bottom

        tk.Button(
            self.sidebar,
            text="🚪   Logout",
            command=self.logout,
            bg=self.dark_green,
            fg="white",
            activebackground="#991B1B",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            anchor="w",
            padx=20,
            cursor="hand2"
        ).pack(
            side="bottom",
            fill="x",
            padx=10,
            pady=20,
            ipady=10
        )


        # MAIN AREA


        self.main_frame = tk.Frame(
            self.root,
            bg=self.background
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.home_page()


    # CLEAR MAIN


    def clear_main(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()


    # HEADER


    def create_header(
        self,
        title,
        subtitle=""
    ):

        header = tk.Frame(
            self.main_frame,
            bg=self.background
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        tk.Label(
            header,
            text=title,
            font=("Arial", 25, "bold"),
            bg=self.background,
            fg=self.text_dark
        ).pack(
            side="left"
        )

        if self.current_user:

            name = self.current_user.get(
                "Name",
                "User"
            )

            tk.Label(
                header,
                text=f"👤 {name}",
                font=("Arial", 11, "bold"),
                bg=self.background,
                fg=self.green
            ).pack(
                side="right"
            )

        if subtitle:

            tk.Label(
                self.main_frame,
                text=subtitle,
                font=("Arial", 10),
                bg=self.background,
                fg=self.text_gray
            ).pack(
                anchor="w",
                padx=30
            )


    # HOME


    def home_page(self):

        self.clear_main()

        self.create_header(
            "Welcome Back 👋",
            "Together we can reduce food waste and rescue food."
        )


        # BANNER


        banner = tk.Frame(
            self.main_frame,
            bg=self.light_green
        )

        banner.pack(
            fill="x",
            padx=30,
            pady=15
        )

        left = tk.Frame(
            banner,
            bg=self.light_green
        )

        left.pack(
            side="left",
            padx=25,
            pady=20
        )

        tk.Label(
            left,
            text="Good Food Should Never Go To Waste 🌱",
            font=("Arial", 18, "bold"),
            bg=self.light_green,
            fg=self.dark_green
        ).pack(
            anchor="w"
        )

        tk.Label(
            left,
            text="Donate food. Help people. Make an impact.",
            font=("Arial", 11),
            bg=self.light_green,
            fg=self.green
        ).pack(
            anchor="w",
            pady=5
        )

        tk.Label(
            banner,
            text="🥕  🍎  🥖  🥛  🥦",
            font=("Arial", 35),
            bg=self.light_green
        ).pack(
            side="right",
            padx=30
        )


        # CARDS


        donations = self.donation_manager.donations

        total = len(donations)

        rescued = 0
        urgent = 0
        completed = 0

        for donation in donations.values():

            if donation.get("status") == "Completed":

                rescued += donation.get(
                    "quantity",
                    0
                )

                completed += 1

            priority = donation.get(
                "priority"
            )

            if priority in [
                "Urgent",
                "Expire"
            ]:

                urgent += 1

        cards = tk.Frame(
            self.main_frame,
            bg=self.background
        )

        cards.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.create_stat_card(
            cards,
            "🍱",
            "Total Donations",
            str(total),
            self.light_green,
            0
        )

        self.create_stat_card(
            cards,
            "♻️",
            "Food Rescued",
            f"{rescued} KG",
            self.blue,
            1
        )

        self.create_stat_card(
            cards,
            "🚨",
            "Urgent Donations",
            str(urgent),
            self.red,
            2
        )

        self.create_stat_card(
            cards,
            "✅",
            "Completed",
            str(completed),
            self.purple,
            3
        )


        # RECENT DONATIONS


        tk.Label(
            self.main_frame,
            text="Recent Donations",
            font=("Arial", 17, "bold"),
            bg=self.background,
            fg=self.text_dark
        ).pack(
            anchor="w",
            padx=30,
            pady=(20, 5)
        )

        self.create_donation_table(
            self.main_frame,
            limit=7
        )


    # STAT CARD


    def create_stat_card(
        self,
        parent,
        icon,
        title,
        value,
        bg_color,
        column
    ):

        card = tk.Frame(
            parent,
            bg=bg_color,
            height=120
        )

        card.grid(
            row=0,
            column=column,
            padx=8,
            sticky="nsew"
        )

        parent.grid_columnconfigure(
            column,
            weight=1
        )

        tk.Label(
            card,
            text=icon,
            font=("Arial", 25),
            bg=bg_color
        ).pack(
            pady=(15, 0)
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 10, "bold"),
            bg=bg_color,
            fg=self.text_dark
        ).pack()

        tk.Label(
            card,
            text=value,
            font=("Arial", 20, "bold"),
            bg=bg_color,
            fg=self.dark_green
        ).pack(
            pady=5
        )


    # DONATIONS PAGE


    def donations_page(self):

        self.clear_main()

        self.create_header(
            "🍱 Donations",
            "Create and manage food donations."
        )

        buttons = tk.Frame(
            self.main_frame,
            bg=self.background
        )

        buttons.pack(
            anchor="w",
            padx=30,
            pady=15
        )

        tk.Button(
            buttons,
            text="+  Create Donation",
            command=self.create_donation_window,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="🔍  Search",
            command=self.search_donation_window,
            bg="#2563EB",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        self.create_donation_table(
            self.main_frame
        )


    # DONATION TABLE


    def create_donation_table(
        self,
        parent,
        limit=None
    ):

        frame = tk.Frame(
            parent,
            bg="white"
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columns = (
            "ID",
            "Donor",
            "Food",
            "Quantity",
            "Location",
            "Expiry",
            "Priority",
            "Status"
        )

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=105,
                anchor="center"
            )

        donations = list(
            self.donation_manager.donations.values()
        )

        if limit:

            donations = donations[-limit:]

        for donation in donations:

            tree.insert(
                "",
                "end",
                values=(
                    donation.get(
                        "donation_id",
                        ""
                    ),
                    donation.get(
                        "donor_name",
                        ""
                    ),
                    donation.get(
                        "food_type",
                        ""
                    ),
                    donation.get(
                        "quantity",
                        ""
                    ),
                    donation.get(
                        "location",
                        ""
                    ),
                    donation.get(
                        "expiry_date",
                        ""
                    ),
                    donation.get(
                        "priority",
                        "Not Calculated"
                    ),
                    donation.get(
                        "status",
                        ""
                    )
                )
            )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


    # CREATE DONATION


    def create_donation_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "DonEat - Create Donation"
        )

        window.geometry(
            "520x650"
        )

        window.configure(
            bg=self.background
        )

        tk.Label(
            window,
            text="🍱 Create New Donation",
            font=("Arial", 22, "bold"),
            bg=self.background,
            fg=self.dark_green
        ).pack(
            pady=25
        )

        fields = [
            "Donor Name",
            "Food Type",
            "Quantity",
            "Location",
            "Expiry Date (YYYY-MM-DD)"
        ]

        entries = []

        for field in fields:

            tk.Label(
                window,
                text=field,
                font=("Arial", 10, "bold"),
                bg=self.background,
                fg=self.text_dark
            ).pack(
                anchor="w",
                padx=60,
                pady=(7, 3)
            )

            entry = tk.Entry(
                window,
                font=("Arial", 10),
                relief="solid",
                bd=1
            )

            entry.pack(
                fill="x",
                padx=60,
                ipady=6
            )

            entries.append(entry)

        def save():

            donor = entries[0].get().strip()
            food_type = entries[1].get().strip()
            quantity = entries[2].get().strip()
            location = entries[3].get().strip()
            expiry = entries[4].get().strip()

            if not all([
                donor,
                food_type,
                quantity,
                location,
                expiry
            ]):

                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )

                return

            if not quantity.isdigit():

                messagebox.showerror(
                    "Error",
                    "Quantity must be a number."
                )

                return

            try:

                datetime.strptime(
                    expiry,
                    "%Y-%m-%d"
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Date must be YYYY-MM-DD."
                )

                return

            donation_id = (
                self.donation_manager.generate_id()
            )

            priority = (
                self.priority_manager
                .calculate_priority(
                    expiry
                )
            )

            donation = {

                "donation_id":
                    donation_id,

                "donor_name":
                    donor,

                "food_type":
                    food_type,

                "quantity":
                    int(quantity),

                "location":
                    location,

                "expiry_date":
                    expiry,

                "priority":
                    priority,

                "status":
                    "Pending"
            }

            self.donation_manager.donations[
                donation_id
            ] = donation

            self.donation_manager.save_donations()

            messagebox.showinfo(
                "Donation Created",
                f"Donation ID: {donation_id}\n"
                f"Priority: {priority}"
            )

            window.destroy()

            self.donations_page()

        tk.Button(
            window,
            text="ADD DONATION",
            command=save,
            bg=self.green,
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        ).pack(
            fill="x",
            padx=60,
            pady=30,
            ipady=8
        )


    # SEARCH


    def search_donation_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Search Donation"
        )

        window.geometry(
            "550x500"
        )

        window.configure(
            bg=self.background
        )

        tk.Label(
            window,
            text="🔍 Search Donation",
            font=("Arial", 22, "bold"),
            bg=self.background,
            fg=self.dark_green
        ).pack(
            pady=25
        )

        entry = tk.Entry(
            window,
            font=("Arial", 12)
        )

        entry.pack(
            padx=50,
            fill="x",
            ipady=7
        )

        result = tk.Text(
            window,
            height=15,
            font=("Arial", 11)
        )

        result.pack(
            padx=50,
            pady=20,
            fill="both",
            expand=True
        )

        def search():

            donation_id = entry.get().strip()

            donations = (
                self.donation_manager.donations
            )

            if donation_id not in donations:

                messagebox.showerror(
                    "Error",
                    "Donation not found."
                )

                return

            d = donations[
                donation_id
            ]

            result.delete(
                "1.0",
                tk.END
            )

            result.insert(
                tk.END,
                f"🍱 DONATION DETAILS\n\n"
                f"ID: {d.get('donation_id')}\n"
                f"Donor: {d.get('donor_name')}\n"
                f"Food: {d.get('food_type')}\n"
                f"Quantity: {d.get('quantity')} KG\n"
                f"Location: {d.get('location')}\n"
                f"Expiry: {d.get('expiry_date')}\n"
                f"Priority: {d.get('priority')}\n"
                f"Status: {d.get('status')}\n"
            )

        tk.Button(
            window,
            text="SEARCH",
            command=search,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(
            pady=5,
            ipadx=20,
            ipady=5
        )


    # REQUESTS


    def requests_page(self):

        self.clear_main()

        self.create_header(
            "👥 Donation Requests",
            "Manage recipient requests and delivery status."
        )

        buttons = tk.Frame(
            self.main_frame,
            bg=self.background
        )

        buttons.pack(
            anchor="w",
            padx=30,
            pady=15
        )

        tk.Button(
            buttons,
            text="+ Request Donation",
            command=self.request_donation_window,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="Update Status",
            command=self.update_request_window,
            bg="#2563EB",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8
        ).pack(
            side="left",
            padx=5
        )

        frame = tk.Frame(
            self.main_frame,
            bg="white"
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columns = (
            "Request ID",
            "Donation ID",
            "Recipient ID",
            "Status"
        )

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                anchor="center",
                width=180
            )

        for request in (
            self.recipient_manager
            .requests.values()
        ):

            tree.insert(
                "",
                "end",
                values=(
                    request.get(
                        "request_id"
                    ),
                    request.get(
                        "donation_id"
                    ),
                    request.get(
                        "recipient_id"
                    ),
                    request.get(
                        "status"
                    )
                )
            )

        tree.pack(
            fill="both",
            expand=True
        )


    # REQUEST DONATION


    def request_donation_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Request Donation"
        )

        window.geometry(
            "450x400"
        )

        window.configure(
            bg=self.background
        )

        tk.Label(
            window,
            text="👥 Request Donation",
            font=("Arial", 22, "bold"),
            bg=self.background,
            fg=self.dark_green
        ).pack(
            pady=25
        )

        labels = [
            "Request ID",
            "Donation ID",
            "Recipient ID"
        ]

        entries = []

        for label in labels:

            tk.Label(
                window,
                text=label,
                bg=self.background,
                fg=self.text_dark,
                font=("Arial", 10, "bold")
            ).pack(
                pady=(8, 3)
            )

            entry = tk.Entry(
                window
            )

            entry.pack(
                ipadx=50,
                ipady=5
            )

            entries.append(entry)

        def submit():

            request_id = entries[0].get().strip()
            donation_id = entries[1].get().strip()
            recipient_id = entries[2].get().strip()

            if not request_id or not donation_id or not recipient_id:

                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )

                return

            success = (
                self.recipient_manager
                .request_donation(
                    request_id,
                    donation_id,
                    recipient_id
                )
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Donation request created!"
                )

                window.destroy()

                self.requests_page()

            else:

                messagebox.showerror(
                    "Error",
                    "Request ID already exists."
                )

        tk.Button(
            window,
            text="SUBMIT REQUEST",
            command=submit,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(
            pady=25,
            ipadx=20,
            ipady=7
        )


    # UPDATE STATUS


    def update_request_window(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Update Request Status"
        )

        window.geometry(
            "400x300"
        )

        window.configure(
            bg=self.background
        )

        tk.Label(
            window,
            text="🔄 Update Status",
            font=("Arial", 22, "bold"),
            bg=self.background,
            fg=self.dark_green
        ).pack(
            pady=25
        )

        entry = tk.Entry(
            window,
            width=30
        )

        entry.pack(
            ipady=7
        )

        tk.Label(
            window,
            text="Enter Request ID",
            bg=self.background
        ).pack(
            pady=8
        )

        def update():

            request_id = entry.get().strip()

            success = (
                self.recipient_manager
                .advance_status(
                    request_id
                )
            )

            if success:

                status = (
                    self.recipient_manager
                    .requests[
                        str(request_id)
                    ]["status"]
                )

                messagebox.showinfo(
                    "Success",
                    f"Status changed to {status}"
                )

                window.destroy()

                self.requests_page()

            else:

                messagebox.showerror(
                    "Error",
                    "Request not found or completed."
                )

        tk.Button(
            window,
            text="UPDATE",
            command=update,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(
            pady=20,
            ipadx=30,
            ipady=7
        )


    # SMART PRIORITY


    def priority_page(self):

        self.clear_main()

        self.create_header(
            "⭐ Smart Priority",
            "Priority is calculated automatically according to expiry date."
        )

        # Calculate priority

        for donation in (
            self.donation_manager.donations.values()
        ):

            expiry = donation.get(
                "expiry_date",
                ""
            )

            donation[
                "priority"
            ] = (
                self.priority_manager
                .calculate_priority(
                    expiry
                )
            )

        self.donation_manager.save_donations()

        # Priority explanation

        info = tk.Frame(
            self.main_frame,
            bg="white"
        )

        info.pack(
            fill="x",
            padx=30,
            pady=15
        )

        priorities = [
            ("🔴 Urgent", "1 day or less", self.red),
            ("🟠 High", "2-3 days", "#FFEDD5"),
            ("🟡 Medium", "4-7 days", self.yellow),
            ("🟢 Low", "More than 7 days", self.light_green),
            ("⚫ Expire", "Already expired", "#E5E7EB")
        ]

        for name, text, color in priorities:

            box = tk.Frame(
                info,
                bg=color
            )

            box.pack(
                side="left",
                padx=5,
                pady=10,
                expand=True,
                fill="x"
            )

            tk.Label(
                box,
                text=name,
                font=("Arial", 10, "bold"),
                bg=color
            ).pack()

            tk.Label(
                box,
                text=text,
                font=("Arial", 8),
                bg=color
            ).pack()

        # Table

        frame = tk.Frame(
            self.main_frame,
            bg="white"
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        columns = (
            "ID",
            "Food",
            "Quantity",
            "Expiry",
            "Priority",
            "Status"
        )

        tree = ttk.Treeview(
            frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                anchor="center",
                width=150
            )

        for donation in (
            self.donation_manager
            .donations.values()
        ):

            tree.insert(
                "",
                "end",
                values=(
                    donation.get(
                        "donation_id"
                    ),
                    donation.get(
                        "food_type"
                    ),
                    donation.get(
                        "quantity"
                    ),
                    donation.get(
                        "expiry_date"
                    ),
                    donation.get(
                        "priority"
                    ),
                    donation.get(
                        "status"
                    )
                )
            )

        tree.pack(
            fill="both",
            expand=True
        )


    # ANALYTICS


    def analytics_page(self):

        self.clear_main()

        self.create_header(
            "📊 Analytics",
            "Analyze donations and food rescue performance."
        )

        self.analyzer = DataAnalyzer()

        report = self.analyzer.generate_report()

        cards = tk.Frame(
            self.main_frame,
            bg=self.background
        )

        cards.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.create_stat_card(
            cards,
            "🍱",
            "Donations",
            str(
                report[
                    "total_donations"
                ]
            ),
            self.light_green,
            0
        )

        self.create_stat_card(
            cards,
            "♻️",
            "Food Rescued",
            f"{report['total_food_rescued']} KG",
            self.blue,
            1
        )

        largest = report[
            "largest_donation"
        ]

        largest_quantity = 0

        if largest:

            largest_quantity = largest.get(
                "quantity",
                0
            )

        self.create_stat_card(
            cards,
            "🏆",
            "Largest Donation",
            f"{largest_quantity} KG",
            self.yellow,
            2
        )

        self.create_stat_card(
            cards,
            "📈",
            "Food Types",
            str(
                len(
                    report[
                        "food_by_type"
                    ]
                )
            ),
            self.purple,
            3
        )

        # Chart button - placed and packed BEFORE the report frame,
        # anchored to the bottom of main_frame, so it always stays
        # visible regardless of how much text the report contains.

        tk.Button(
            self.main_frame,
            text="📊  View Food Charts",
            command=self.show_food_chart,
            bg=self.green,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat"
        ).pack(
            side="bottom",
            pady=15,
            ipadx=20,
            ipady=7
        )

        # Report


        report_frame = tk.Frame(
            self.main_frame,
            bg="white"
        )

        report_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        text = tk.Text(
            report_frame,
            font=("Arial", 11),
            bg="white",
            fg=self.text_dark,
            relief="flat"
        )

        text.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        text.insert(
            tk.END,
            "🍽️  D O N E A T   R E P O R T\n"
        )

        text.insert(
            tk.END,
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

        text.insert(
            tk.END,
            f"🍱 Total Donations: "
            f"{report['total_donations']}\n\n"
        )

        text.insert(
            tk.END,
            f"♻️ Total Food Rescued: "
            f"{report['total_food_rescued']} KG\n\n"
        )

        text.insert(
            tk.END,
            "🍎 Food By Type:\n"
        )

        for food, quantity in (
            report[
                "food_by_type"
            ].items()
        ):

            text.insert(
                tk.END,
                f"   • {food}: {quantity} KG\n"
            )

        text.insert(
            tk.END,
            "\n📦 Status Statistics:\n"
        )

        for status, count in (
            report[
                "status_statistics"
            ].items()
        ):

            text.insert(
                tk.END,
                f"   • {status}: {count}\n"
            )

        text.insert(
            tk.END,
            "\n⭐ Priority Statistics:\n"
        )

        for priority, count in (
            report[
                "priority_statistics"
            ].items()
        ):

            text.insert(
                tk.END,
                f"   • {priority}: {count}\n"
            )


    # CHART


    def show_food_chart(self):

        analyzer = DataAnalyzer()

        report = analyzer.generate_report()

        food_types = list(
            report[
                "food_by_type"
            ].keys()
        )

        quantities = list(
            report[
                "food_by_type"
            ].values()
        )

        if not food_types:

            messagebox.showinfo(
                "No Data",
                "No donation data available."
            )

            return

        # Colors for each food type, cycling through the palette

        food_colors = [
            self.chart_palette[i % len(self.chart_palette)]
            for i in range(len(food_types))
        ]

        status_data = report.get(
            "status_statistics",
            {}
        )

        status_labels = list(status_data.keys())
        status_values = list(status_data.values())

        status_colors = [
            self.chart_palette[i % len(self.chart_palette)]
            for i in range(len(status_labels))
        ]

        priority_data = report.get(
            "priority_statistics",
            {}
        )

        priority_order = [
            "Urgent",
            "High",
            "Medium",
            "Low",
            "Expire"
        ]

        priority_colors_map = {
            "Urgent": "#EF4444",
            "High": "#F97316",
            "Medium": "#F59E0B",
            "Low": "#10B981",
            "Expire": "#6B7280"
        }

        priority_labels = [
            key for key in priority_order
            if key in priority_data
        ]

        priority_labels += [
            key for key in priority_data
            if key not in priority_order
        ]

        priority_values = [
            priority_data[key] for key in priority_labels
        ]

        priority_colors = [
            priority_colors_map.get(
                key,
                "#94A3B8"
            )
            for key in priority_labels
        ]

        # Build a 2x2 dashboard of different, colorful chart types

        fig, axes = plt.subplots(
            2,
            2,
            figsize=(11, 8)
        )

        fig.suptitle(
            "DonEat - Food Donation Analytics",
            fontsize=16,
            fontweight="bold",
            color="#064E3B"
        )

        # 1) Bar chart - quantity by food type

        ax1 = axes[0][0]

        ax1.bar(
            food_types,
            quantities,
            color=food_colors
        )

        ax1.set_title(
            "Quantity by Food Type"
        )

        ax1.set_xlabel("Food Type")
        ax1.set_ylabel("Quantity (KG)")
        ax1.tick_params(axis="x", rotation=30)

        # 2) Pie chart - share of quantity by food type

        ax2 = axes[0][1]

        if sum(quantities) > 0:

            ax2.pie(
                quantities,
                labels=food_types,
                colors=food_colors,
                autopct="%1.0f%%",
                startangle=90
            )

        else:

            ax2.text(
                0.5,
                0.5,
                "No quantity data",
                ha="center",
                va="center"
            )

        ax2.set_title(
            "Food Type Share"
        )

        # 3) Donut chart - donation status breakdown

        ax3 = axes[1][0]

        if status_labels and sum(status_values) > 0:

            wedges, _ = ax3.pie(
                status_values,
                colors=status_colors,
                startangle=90,
                wedgeprops=dict(width=0.4)
            )

            ax3.legend(
                wedges,
                status_labels,
                loc="center",
                fontsize=8
            )

        else:

            ax3.text(
                0.5,
                0.5,
                "No status data",
                ha="center",
                va="center"
            )

        ax3.set_title(
            "Donation Status"
        )

        # 4) Horizontal bar chart - priority breakdown

        ax4 = axes[1][1]

        if priority_labels:

            ax4.barh(
                priority_labels,
                priority_values,
                color=priority_colors
            )

            ax4.set_xlabel("Number of Donations")

        else:

            ax4.text(
                0.5,
                0.5,
                "No priority data",
                ha="center",
                va="center"
            )

        ax4.set_title(
            "Priority Breakdown"
        )

        plt.tight_layout(
            rect=[0, 0, 1, 0.95]
        )

        plt.show()


    # LOGOUT


    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:

            self.current_user = None

            self.login_screen()



# RUN


if __name__ == "__main__":

    root = tk.Tk()

    app = DonEatGUI(
        root
    )

    root.mainloop()