#This script was written by Anonemous2 8/18/2022

#import os subprocess module
import os
#import json module
import json
from json.decoder import JSONDecodeError

# Handles All Titans base units that I want to be selectable commanders
# Each unit is manually added to the list (as we don't want structures, and unconventional units added)
def main():
    # starts by asking for correct directory to media PA
    # use default, then ask if the user wants to change it.
    if 1 == 0:
        media_dir = "C:/Program Files (x86)/Steam/steamapps/common/Planetary Annihilation Titans/media"
    else:
        media_dir = "B:/SteamLibrary/steamapps/common/Planetary Annihilation Titans/media"
    print("Is the following directory correct? (y/n): " + media_dir)
    user_input = str(input())
    if (user_input.lower()) == "n":
        while user_input.lower() != "y":
            print("Enter new media directory: ")
            media_dir = str(input())
            media_dir = media_dir.replace('\\', '/')
            print("Is the following directory correct? (y/n): " + media_dir)
            user_input = str(input())

    # setup unit mod folder
    # find current directory
    home_dir = os.path.dirname(os.path.realpath(__file__))
    home_dir = home_dir.replace('\\', '/')
    print(home_dir)

    # Copy over commanders list
    file = open(media_dir + "/pa_ex1/units/commanders/commander_list.json")
    file_data = json.load(file)
    # Write to new file
    new_file = open(home_dir + "/pa/units/commanders/commander_list.json", "w+")
    print(json.dumps(file_data))
    new_file.write(json.dumps(file_data))
    new_file.close()
    file.close()

    # Vehicles
    add_to_commanders("/units/land/aa_missile_vehicle/aa_missile_vehicle.json", "profile_spinner.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/attack_vehicle/attack_vehicle.json", "profile_stryker.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/land_scout/land_scout.json", "profile_skidder.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_armor/tank_armor.json", "profile_inferno.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_flak/tank_flak.json", "profile_storm.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_heavy_armor/tank_heavy_armor.json", "profile_vanguard.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_heavy_mortar/tank_heavy_mortar.json", "profile_sheller.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_hover/tank_hover.json", "profile_drifter.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_laser_adv/tank_laser_adv.json", "profile_leveler.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_light_laser/tank_light_laser.json", "profile_ant.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/tank_nuke/tank_nuke.json", "profile_nuke.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/titan_vehicle/titan_vehicle.json", "profile_ares.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    # Bots
    add_to_commanders("/units/land/assault_bot/assault_bot.json", "profile_dox.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/assault_bot_adv/assault_bot_adv.json", "profile_slammer.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_aa/bot_aa.json", "profile_stinger.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_bomb/bot_bomb.json", "profile_boom.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_grenadier/bot_grenadier.json", "profile_grenadier.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_nanoswarm/bot_nanoswarm.json", "profile_locust.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_sniper/bot_sniper.json", "profile_gile.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_support_commander/bot_support_commander.json", "profile_subcom.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_tactical_missile/bot_tactical_missile.json", "profile_bluehawk.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/bot_tesla/bot_tesla.json", "profile_tesla.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/titan_bot/titan_bot.json", "profile_atlas.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    # Air
    add_to_commanders("/units/air/air_scout/air_scout.json", "profile_firefly.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/bomber/bomber.json", "profile_bubblebee.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/bomber_adv/bomber_adv.json", "profile_hornet.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/bomber_heavy/bomber_heavy.json", "profile_wyrm.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/fighter/fighter.json", "profile_fighter.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/fighter_adv/fighter_adv.json", "profile_adv_fighter.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/gunship/gunship.json", "profile_gunship.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/solar_drone/solar_drone.json", "profile_icarus.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/strafer/strafer.json", "profile_horsefly.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/titan_air/titan_air.json", "profile_zues.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/transport/transport.json", "profile_pelican.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/support_platform/support_platform.json", "profile_angel.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    # Orbital
    add_to_commanders("/units/orbital/orbital_battleship/orbital_battleship.json", "profile_omega.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_fighter/orbital_fighter.json", "profile_avenger.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_lander/orbital_lander.json", "profile_astraus.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_laser/orbital_laser.json", "profile_ssx.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_probe/orbital_probe.json", "profile_hermes.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_railgun/orbital_railgun.json", "profile_artemis.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/radar_satellite/radar_satellite.json", "profile_radar.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/radar_satellite_adv/radar_satellite_adv.json", "profile_adv_radar.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/solar_array/solar_array.json", "profile_solar.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/titan_orbital/titan_orbital.json", "profile_helios.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    media_dir = "B:/SteamLibrary/steamapps/common/Planetary Annihilation Titans/media"
    print("Please enter SW's directory.")
    user_input = "n"
    if (user_input.lower()) == "n":
        while user_input.lower() != "y":
            print("Enter new media directory: ")
            media_dir = str(input())
            media_dir = media_dir.replace('\\', '/')
            print("Is the following directory correct? (y/n): " + media_dir)
            user_input = str(input())

    # All fabs need to disabled customs build
    add_to_commanders("/units/land/fabrication_vehicle/fabrication_vehicle.json", "profile_vehicle_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/fabrication_vehicle_adv/fabrication_vehicle_adv.json", "profile_adv_vehicle_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/fabrication_bot/fabrication_bot.json", "profile_bot_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/fabrication_bot_adv/fabrication_bot_adv.json", "profile_adv_bot_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/fabrication_bot_combat/fabrication_bot_combat.json", "profile_stitch.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/land/fabrication_bot_combat_adv/fabrication_bot_combat_adv.json", "profile_mend.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/fabrication_aircraft/fabrication_aircraft.json", "profile_air_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/air/fabrication_aircraft_adv/fabrication_aircraft_adv.json", "profile_adv_air_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

    add_to_commanders("/units/orbital/orbital_fabrication_bot/orbital_fabrication_bot.json", "profile_orb_fab.png", "img_bots.png",
                      "img_bots_thumb.png", home_dir, media_dir, "/pa/units/commanders/commander_list.json")

# Look in pa_ex1 first of the listed unit, if not found, pull from pa
# After updating the unit, add to the commander's list
def add_to_commanders(unit_file, prof_img, img, thumb_img, h_dir, m_dir, com_list):
    try:
        # Update the image paths
        prof_img = "/ui/main/shared/img/commanders/profiles/" + prof_img
        img = "/ui/main/shared/img/commanders/" + img
        thumb_img = "/ui/main/shared/img/commanders/thumbs/" + thumb_img

        # Attempt to open the ex1 version
        try:
            with open(m_dir + "/pa_ex1" + unit_file) as file:
                file_data = json.load(file)
        except FileNotFoundError:
            with open(m_dir + "/pa" + unit_file) as file:
                file_data = json.load(file)
        finally:
            # Update the file
            data_append = {"catalog_object_name": "InvictusCommander"}
            file_data.update(data_append)
            data_append = {"client": {"ui": {"image": img, "thumb_image": thumb_img, "profile_image": prof_img}}}
            file_data.update(data_append)

            # Write to new file
            new_file = open(h_dir + "/pa" + unit_file, "w+")
            print(json.dumps(file_data))
            new_file.write(json.dumps(file_data))

            new_file.close()
            file.close()

            # Now update the commander list
            file = open(h_dir + com_list)
            file_data = file.read()

            com_data = file_data.replace("]", ", \"/pa" + unit_file + "\"]")

            new_file = open(h_dir + com_list, "w+")
            print(com_data)
            new_file.write(com_data)
            new_file.close()

    except UnicodeDecodeError as error:
        print(error)
    except JSONDecodeError as error:
        print(error)



main()

#end of program
print("---END---")