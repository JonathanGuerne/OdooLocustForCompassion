from locust import task, between, events
from OdooLocust.OdooLocustUser import OdooLocustUser

from random import choice

LOGIN = None
PASSWORD = None
DATABASE = None


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--login", type=str, env_var="LOGIN", default="", help="user used to connect to odoo")
    parser.add_argument("--password", type=str, env_var="PASSWORD", default="", help="password of the user")
    parser.add_argument("--database", type=str, env_var="DATABASE", default="", help="odoo database to connect to")


@events.init.add_listener
def _(environment, **kw):
    global LOGIN, PASSWORD, DATABASE
    LOGIN = environment.parsed_options.login
    PASSWORD = environment.parsed_options.password
    DATABASE = environment.parsed_options.database


class RPC(OdooLocustUser):
    wait_time = between(5, 10)


    def on_start(self):
        if ":" in self.host:
            self.host = self.host.split(":")[0] 
        
        self.login = LOGIN or self.login 
        self.password = PASSWORD or self.password 
        self.database = DATABASE or self.database 

        return super().on_start()

    @task(10)
    def mycompassion(self):
        contract_model = self.client.get_model('recurring.contract')
        ids = contract_model.search([])
        contract = contract_model.read(choice(ids))
        child_model = self.client.get_model("compassion.child")
        ids = child_model.search([("id", "=", contract["child_id"][0])])
        child = child_model.read(ids)


    @task(5)
    def read_communication(self):
        comm_model = self.client.get_model('partner.communication.job')
        comm_ids = comm_model.search([])
        prtns = comm_model.read(choice(comm_ids))          
        
    @task(3)
    def read_account_journal(self):
        journal_model = self.client.get_model('account.journal')
        journal_ids = journal_model.search([])
        prtns = journal_model.read(choice(journal_ids))      


    @task(10)
    def read_partners(self):
        cust_model = self.client.get_model('res.partner')
        cust_ids = cust_model.search([])
        prtns = cust_model.read(choice(cust_ids))


    @task(7)
    def read_contracts(self):
        prod_model = self.client.get_model('recurring.contract')
        ids = prod_model.search([])
        prods = prod_model.read(choice(ids))
