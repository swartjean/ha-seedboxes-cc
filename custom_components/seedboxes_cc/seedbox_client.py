import aiohttp

from .const import (
    NAME_DISK_QUOTA_FREE,
    NAME_DISK_QUOTA_USED,
    NAME_DISK_QUOTA_USED_PCT,
    NAME_DISK_SIZE,
    NAME_IP_ADDRESS,
    NAME_MONTHLY_TRAFFIC,
    NAME_STATUS,
    NAME_TORRENT_CLIENT,
)


class seedbox_client:
    """Interface class to obtain client information using the Seedboxes.cc API"""

    def __init__(self, api_key):
        """Initializes class parameters"""

        self.base_url = "https://www.seedboxes.cc/api/client"
        self.api_key = api_key
        self.headers = {
            "user_agent": "Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
            "Authorization": f"Token token={self.api_key}",
        }

    async def async_query_api(self, endpoint="", payload=None):
        """Queries a given endpoint on the Seedboxes.cc API with the specified payload

        Args:
            endpoint (string, optional): The endpoint of the Seedboxes.cc API. Defaults to ""
            payload (dict, optional): The parameters to apply to the query. Defaults to None.

        Returns:
            The response object from the request in JSON format
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url=self.base_url + endpoint, headers=self.headers, params=payload,
            ) as res:
                # Raise an exception for an invalid token
                if res.status == 401:
                    raise Exception("Invalid Seedboxes.cc API Key")

                return await res.json()

    def get_disk_quota_used_percent(self, res):
        return round(
            100
            * (res["products"][0]["seedbox"]["latest_stats"]["diskspace"] / 1000)
            / res["products"][0]["seedbox"]["disk_space"],
            2,
        )

    def get_disk_quota_free(self, res):
        return round(
            res["products"][0]["seedbox"]["disk_space"]
            - (res["products"][0]["seedbox"]["latest_stats"]["diskspace"] / 1000),
            2,
        )

    def get_disk_quota_used(self, res):
        return round(
            res["products"][0]["seedbox"]["latest_stats"]["diskspace"] / 1000, 2,
        )

    def get_monthly_traffic(self, res):
        return round(
            res["products"][0]["seedbox"]["latest_stats"]["traffic"] / 1024, 2,
        )

    async def async_get_data(self):
        """Fetches all available data from the Seedboxes.cc API"""
        res = await self.async_query_api()

        # Format the data object using the response JSON
        try:
            data = {
                "data": {
                    NAME_DISK_QUOTA_FREE: float(self.get_disk_quota_free(res)),
                    NAME_DISK_QUOTA_USED: float(self.get_disk_quota_used(res)),
                    NAME_DISK_QUOTA_USED_PCT: float(
                        self.get_disk_quota_used_percent(res)
                    ),
                    NAME_MONTHLY_TRAFFIC: float(self.get_monthly_traffic(res)),
                    NAME_DISK_SIZE: float(res["products"][0]["seedbox"]["disk_space"]),
                    NAME_IP_ADDRESS: res["products"][0]["seedbox"]["server"]["ip"],
                    NAME_TORRENT_CLIENT: res["products"][0]["seedbox"][
                        "torrent_client"
                    ],
                    NAME_STATUS: res["products"][0]["status"],
                },
            }
            return data
        except KeyError as e:
            # Catch a key error while parsing the returned JSON and re-raise it as a more understandable exception
            raise Exception(
                f"Error parsing JSON response from Seedboxes.cc API, bad key: {e}"
            ) from e
