# Pi network configuration

Instructions on how to connect the Pi to a wifi network.

_NB_  
This configuration will enable wifi network and it will be accessible when testing from the terminal.  
For some uknown reason this configuration will not bubble up to the Ubuntu desktop layer, and the gui apps will not be able to connect to anything.

## BYOD Raspberry

_Prereq_  
Read up on [BYOD rules for Equinor](https://insight.equinor.com/sites/information-technology/SitePage/59798/wireless-network-password)  

1. Open a browser in an on-prem network and find your personal wifi password [here](https://insight.equinor.com/sites/information-technology/SitePage/59798/wireless-network-password)

1. Hash the password  
    `echo -n 'password-string' | iconv -t utf16le | openssl md4`  
    Please use `'` to wrap the password string to ensure that bash will read it as string.  
    If you use `"` then you will run into trouble with special chars, which will lead you to escaping said chars, which will lead to escape chars to be included in the hash, which will lead to wrong password, which will lead further down the rabbit hole...  

1. Update wpa supplicant configuration  
    (open a terminal on the Pi)  

    `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`  

    Change `identity` and `password`
    ```    
    network={
        ssid="Statoil-Approved"
        priority=1
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="your-user@equinor.com"
        password=hash:hashed-pasword-string
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
    }
    ```

1. Update network interfaces to ensure that wifi device use the wpa supplicant configuration    

    `sudo nano /etc/network/interfaces`  
    ```
    auto wlan0

    allow-hotplug wlan0
    iface wlan0 inet dhcp
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    ```

1. Reboot network service to enable new configuration  
    `sudo service networking restart`  

1. Test network connection from terminal
    `ping www.vg.no`  

    If no connection then first try a restart `sudo reboot` and test again (Pis can be fussy...)


## Troubleshooting

### Debugging

You can inspect network component status by using these two commands  
- `journalctl -xe`
- `sudo systemctl status networking.service`


### Missing device

Sometimes the Pi will complain that it cannot find one of the network devices (in my case it was eth0) by name as specified in the network interfaces file.  
Simply find the logical name of the device using command `sudo lshw -C network` and replace the name in the interfaces file, then reboot.