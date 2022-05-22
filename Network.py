import speedtest_cli
import audiobot
def network():
    st = speedtest_cli.Speedtest()
    server_names = []   
    st.get_servers(server_names)

    downlink_bps = st.download()
    uplink_bps = st.upload()
    ping = st.results.ping
    up_mbps = uplink_bps / 1000000
    down_mbps = downlink_bps / 1000000
    txt = f"""
        thời gian ping là {round(ping,2)} mili giây
        tốc độ tải lên {round(up_mbps,2)} megabit/giây
        tốc độ tải xuổng {round(down_mbps,2)} megabit/giây
    """
    audiobot.speak_vn(txt)