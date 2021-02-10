# Generated by Django 3.0.6 on 2020-05-28 19:03

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='date',
            new_name='date_of_accident',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='description',
            new_name='more_accident_info',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='time',
            new_name='time_of_accident',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='age',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='causes',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='currently_allocated_to',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='junction_type',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='number_of_damage_vehicle',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='number_of_death',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='number_of_injury',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='traffic_lane',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='vehicle_involved',
        ),
        migrations.AddField(
            model_name='incident',
            name='category_of_victims',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Driver', 'Driver'), ('Passenger', 'Passenger'), ('Trailer', 'Trailer'), ('Motorcycle', 'Motorcyclist'), ('Tricyclist', 'Tricyclist'), ('Bicyclist', 'Bicyclist'), ('Pedestrian', 'Pedestrian')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='driver_precrash_factors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nothing notable', 'Nothing notable'), ('Fatigue/Sleepiness', 'Fatigue/Sleepiness'), ('Sudden illness', 'Sudden illness'), ('Speeding', 'Speeding'), ('Careless overtaking', 'Careless overtaking'), ('Tailgating', 'Tailgating'), ('Sudden turn', 'Sudden turn'), ('risktaking', 'Other calculated risktaking'), ('phone while driving', 'Use of phone while driving'), ('Alcohol', 'Influence of alcohol'), ('Drug', 'Influence of drug'), ('Other distractions', 'Other distractions/inattentiveness')], default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='gender_of_victims',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Male', 'Male'), ('Female', 'Female')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='number_of_damaged_vehicles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='number_of_deaths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='number_of_injured',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='number_of_vehicles_involved',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='road_geometry',
            field=models.CharField(choices=[('Straight road', 'Straight road'), ('Curve', 'Curve'), ('Roundabout', 'Roundabout'), ('T-junction', 'T-junction'), ('Y-junction', 'Y-junction'), ('+-junction', '+-junction'), ('Bridge', 'Bridge'), ('Road works', 'Road works'), ('Other', 'Other')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='vehicle_precrash_factors',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Tyre burst', 'Tyre burst'), ('Mechanical deficiency', 'Mechanical deficiency'), ('Overloaded', 'Overloaded'), ('Defective light', 'Defective light'), ('Nothing notable', 'Nothing notable')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='victims_age_group',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Baby', 'Baby'), ('Toddler', 'Toddler'), ('Child', 'Child'), ('Teenager', 'Teenager'), ('Adult', 'Adult'), ('Middle aged', 'Middle aged'), ('Elderly', 'Elderly')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='victims_current_location',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Accident Scene'), (2, 'Hospital'), (3, 'Other')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='collision_type',
            field=models.CharField(choices=[('Mv/mv head on', 'Moving vehicles, head on'), ('Mv/mv rear end', 'Moving vehicles, rear end'), ('Mv/mv intersecting', 'Moving vehicles, intersecting'), ('Mv/mv overtake', 'Moving vehicles, overtake'), ('Mv/mv turn', 'Moving vehicles, turn'), ('Single mv hit object', 'Single moving vehicle, hit object'), ('Single mv run off', 'Single moving vehicle, run off'), ('Single mv falling off', 'Single moving vehicle, falling off'), ('Mv/pedestrian', 'Moving vehicle with pedestrian'), ('Mv/bicyclist', 'Moving vehicle with pedestrian'), ('Other', 'Other')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='location',
            field=models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Damaturu', 'Damaturu'), ('Ebonyi', 'Ebonyi'), ('Enugu', 'Enugu'), ('Lagos', 'Lagos'), ('Ogun', 'Ogun')], max_length=45),
        ),
        migrations.AlterField(
            model_name='incident',
            name='number_of_victims',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='road_type',
            field=models.CharField(choices=[('Dual carriageway', 'Dual carriageway'), ('Single carriageway', 'Single carriageway'), ('Expressway', 'Expressway'), ('Street', 'Street'), ('Other', 'Other')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incident',
            name='vehicle_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Car saloon', 'Car saloon'), ('Microbus', 'Microbus (< 10 seater)'), ('Minibus', 'Minibus (< 15 seater)'), ('Coaster', 'Coaster (< 15 > 35 seater)'), ('Bus', 'Bus (> 35 seater)'), ('Pickup', 'Pickup'), ('SUV', 'SUV (Jeep'), ('Light lorry', 'Light lorry (< 3.5 t)'), ('Heavy lorry', 'Heavy lorry (> 3.5 t)'), ('Tanker', 'Tanker'), ('Trailer', 'Trailer'), ('Motorcycle', 'Motorcycle'), ('Tricycle', 'Tricycle'), ('Bicycle', 'Bicycle'), ('Unknown', 'Unknown')], max_length=20),
        ),
    ]
