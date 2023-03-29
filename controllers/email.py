class Email:
    def __init__(self):
        self.source_address: str = "sai.devops@gameloft.com"
        self.to_address: list = ["sai.devops@gameloft.com"]
        self.project_name: str = "<%= @project_name -%>"
        self.env: str = "<%= @env -%>"
        self.main_region: str = "eu-west-1"

    def _init_subject(self) -> str:
        return f"[WARNING] | {self.project_name}-{self.env} | Low Disk space | Disk Usage {self.get_percent_used()}%"

    def _init_content(self) -> str:
        return f"""
        <html>
        <p>Hello there,</p><br>
        <style>
        p {{
            font-family: monospace;
            font-size: 14px;
        }}
        </style>
        <p>You are receiving this email because your EC2 <strong>"{self.get_host_name()}"</strong> in <strong>{self.get_region()}</strong> region is in state that the HDD is almost full</p>
        <p>-----------------------------</p>
        <p>Alarm details:</p>
        <p>- Account ID: {self.get_account_id()}</p>
        <p>- Host name: {self.get_host_name()}</p>
        <p>- IP address: {self.get_public_ip()}</p>
        <p>- Status: Disk Usage {self.get_percent_used()}% ({self.get_disk_used()}/{self.get_full_disk()}Gb)</p>
        <p>- Timestamp: {self.get_timestamp()}</p>
        <p>- Action require: Clean up unused data ASAP.</p><br>
        <p>Best regards,</p>
        <p>SAI DevOps Auto Report</p>
        </html>
        """

    def send(self):
        import boto3

        client = boto3.client("ses", region_name=f"{self.main_region}")
        client.send_email(
            Source=self.source_address,
            Destination={
                "ToAddresses": self.to_address,
            },
            Message={
                "Subject": {
                    "Data": self._init_subject(),
                },
                "Body": {
                    "Html": {
                        "Data": self._init_content(),
                    }
                },
            },
        )
