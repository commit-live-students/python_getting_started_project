import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

def bowled_out(data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
                bowled_players.append(delivery_info['wicket']['player_out'])

    return bowled_players
