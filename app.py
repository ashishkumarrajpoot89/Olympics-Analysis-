# import streamlit as st
# import pandas as pd
# import preprocessor,helper
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.figure_factory as ff

# df = pd.read_csv('athlete_events.csv')

# region_df = pd.read_csv('noc_regions.csv')

# df = preprocessor.preprocess(df,region_df)

# st.markdown("<h1 style='text-align: center;'>🏅OLYMPICS ANALYSIS🏅</h1>", unsafe_allow_html=True)
# st.sidebar.title("Olympics Analysis")
# ##st.sidebar.image('https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
# st.sidebar.image('Olympics-Logo.png')
# user_menu = st.sidebar.radio(
#     'Select an Option',
#     ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
# )

# if user_menu == 'Medal Tally':
#     st.sidebar.header("Medal Tally")
#     years,country = helper.country_year_list(df)

#     selected_year = st.sidebar.selectbox("Select Year",years)
#     selected_country = st.sidebar.selectbox("Select Country", country)

#     medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
#     if selected_year == 'Overall' and selected_country == 'Overall':
#         st.title("Overall Tally")
#     if selected_year != 'Overall' and selected_country == 'Overall':
#         st.title("Medal Tally in " + str(selected_year) + " Olympics")
#     if selected_year == 'Overall' and selected_country != 'Overall':
#         st.title(selected_country + " overall performance")
#     if selected_year != 'Overall' and selected_country != 'Overall':
#         st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
#     st.table(medal_tally)

# if user_menu == 'Overall Analysis':
#     editions = df['Year'].unique().shape[0] - 1
#     cities = df['City'].unique().shape[0]
#     sports = df['Sport'].unique().shape[0]
#     events = df['Event'].unique().shape[0]
#     athletes = df['Name'].unique().shape[0]
#     nations = df['region'].unique().shape[0]

#     st.title("Top Statistics")
#     col1,col2,col3 = st.columns(3)#beta_columns
#     with col1:
#         st.header("Editions")
#         st.title(editions)
#     with col2:
#         st.header("Hosts")
#         st.title(cities)
#     with col3:
#         st.header("Sports")
#         st.title(sports)

#     col1, col2, col3 = st.columns(3)#beta_columns(3)
#     with col1:
#         st.header("Events")
#         st.title(events)
#     with col2:
#         st.header("Nations")
#         st.title(nations)
#     with col3:
#         st.header("Athletes")
#         st.title(athletes)

#     nations_over_time = helper.data_over_time(df,'region')
#     fig = px.line(nations_over_time, x="Edition", y="region")
#     st.title("Participating Nations over the years")
#     st.plotly_chart(fig)

#     events_over_time = helper.data_over_time(df, 'Event')
#     fig = px.line(events_over_time, x="Edition", y="Event")
#     st.title("Events over the years")
#     st.plotly_chart(fig)

#     athlete_over_time = helper.data_over_time(df, 'Name')
#     fig = px.line(athlete_over_time, x="Edition", y="Name")
#     st.title("Athletes over the years")
#     st.plotly_chart(fig)

#     st.title("No. of Events over time(Every Sport)")
#     fig,ax = plt.subplots(figsize=(20,20))
#     x = df.drop_duplicates(['Year', 'Sport', 'Event'])
#     ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
#                 annot=True)
#     st.pyplot(fig)

#     st.title("Most successful Athletes")
#     sport_list = df['Sport'].unique().tolist()
#     sport_list.sort()
#     sport_list.insert(0,'Overall')

#     selected_sport = st.selectbox('Select a Sport',sport_list)
#     x = helper.most_successful(df,selected_sport)
#     st.table(x)



# if user_menu == 'Country-wise Analysis':

#     st.sidebar.title('Country-wise Analysis')

#     # Get the list of countries from the dataset
#     country_list = df['region'].dropna().unique().tolist()
#     country_list.sort()

#     # Sidebar selection for the country
#     selected_country = st.sidebar.selectbox('Select a Country', country_list)

#     # Year-wise Medal Tally
#     st.title(f"{selected_country} Medal Tally Over the Years")
#     country_df = helper.yearwise_medal_tally(df, selected_country)
    
#     if country_df.empty:
#         st.warning(f"No medal data available for {selected_country}.")
#     else:
#         fig = px.line(country_df, x="Year", y="Medal", title=f"{selected_country} Medal Tally")
#         st.plotly_chart(fig)

#     # Country Event Heatmap
#     st.title(f"{selected_country} Excels in the Following Sports")
#     pt = helper.country_event_heatmap(df, selected_country)
    
#     if pt.empty:
#         st.warning(f"No event data available for {selected_country}.")
#     else:
#         fig, ax = plt.subplots(figsize=(20, 20))
#         sns.heatmap(pt, annot=True, ax=ax, cmap="YlGnBu")
#         ax.set_title(f"Performance of {selected_country} in Different Sports Over the Years")
#         st.pyplot(fig)

#     # Top 10 Athletes
#     st.title(f"Top 10 Athletes of {selected_country}")
#     top10_df = helper.most_successful_countrywise(df, selected_country)
    
#     if top10_df.empty:
#         st.warning(f"No athlete data available for {selected_country}.")
#     else:
#         st.table(top10_df)

# if user_menu == 'Athlete wise Analysis':
#     athlete_df = df.drop_duplicates(subset=['Name', 'region'])

#     # Distribution of Age Analysis
#     x1 = athlete_df['Age'].dropna()
#     x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
#     x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
#     x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

#     fig = ff.create_distplot(
#         [x1, x2, x3, x4],
#         ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
#         show_hist=False,
#         show_rug=False
#     )
#     fig.update_layout(autosize=False, width=1000, height=600)
#     st.title("Distribution of Age")
#     st.plotly_chart(fig)

#     # Distribution of Age wrt Sports (Gold Medalist)
#     x = []
#     name = []
#     famous_sports = [
#         'Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
#         'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
#         'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
#         'Water Polo', 'Hockey', 'Rowing', 'Fencing',
#         'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
#         'Tennis', 'Golf', 'Softball', 'Archery',
#         'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
#         'Rhythmic Gymnastics', 'Rugby Sevens',
#         'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey'
#     ]
#     for sport in famous_sports:
#         temp_df = athlete_df[athlete_df['Sport'] == sport]
#         x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
#         name.append(sport)

#     fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
#     fig.update_layout(autosize=False, width=1000, height=600)
#     st.title("Distribution of Age wrt Sports (Gold Medalist)")
#     st.plotly_chart(fig)

#     # Height vs Weight Analysis
#     sport_list = df['Sport'].unique().tolist()
#     sport_list.sort()
#     sport_list.insert(0, 'Overall')

#     st.title('Height Vs Weight')
#     selected_sport = st.selectbox('Select a Sport', sport_list)
#     temp_df = helper.weight_v_height(df, selected_sport)

#     if temp_df.empty:
#         st.warning(f"No data available for {selected_sport}.")
#     else:
#         fig, ax = plt.subplots()
#         sns.scatterplot(
#             data=temp_df,
#             x='Weight',
#             y='Height',
#             hue='Medal',
#             style='Sex',
#             s=60,
#             ax=ax
#         )
#         ax.set_title(f"Height vs Weight Distribution for {selected_sport}")
#         st.pyplot(fig)

#     # Men vs Women Participation Over the Years
#     st.title("Men Vs Women Participation Over the Years")
#     final = helper.men_vs_women(df)
#     fig = px.line(final, x="Year", y=["Male", "Female"])
#     fig.update_layout(autosize=False, width=1000, height=600)
#     st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# Add the file uploader widget to allow users to upload the athlete_events.csv file
uploaded_file = st.file_uploader("Upload athlete_events.csv", type="csv")

# Check if the file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("File loaded successfully!")
    region_df = pd.read_csv('noc_regions.csv')

    df = preprocessor.preprocess(df, region_df)

    st.markdown("<h1 style='text-align: center;'>🏅OLYMPICS ANALYSIS🏅</h1>", unsafe_allow_html=True)
    st.sidebar.title("Olympics Analysis")
    st.sidebar.image('Olympics-Logo.png')
    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
    )

    if user_menu == 'Medal Tally':
        st.sidebar.header("Medal Tally")
        years, country = helper.country_year_list(df)

        selected_year = st.sidebar.selectbox("Select Year", years)
        selected_country = st.sidebar.selectbox("Select Country", country)

        medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
        if selected_year == 'Overall' and selected_country == 'Overall':
            st.title("Overall Tally")
        if selected_year != 'Overall' and selected_country == 'Overall':
            st.title("Medal Tally in " + str(selected_year) + " Olympics")
        if selected_year == 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " overall performance")
        if selected_year != 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        st.table(medal_tally)

    if user_menu == 'Overall Analysis':
        editions = df['Year'].unique().shape[0] - 1
        cities = df['City'].unique().shape[0]
        sports = df['Sport'].unique().shape[0]
        events = df['Event'].unique().shape[0]
        athletes = df['Name'].unique().shape[0]
        nations = df['region'].unique().shape[0]

        st.title("Top Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Editions")
            st.title(editions)
        with col2:
            st.header("Hosts")
            st.title(cities)
        with col3:
            st.header("Sports")
            st.title(sports)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Events")
            st.title(events)
        with col2:
            st.header("Nations")
            st.title(nations)
        with col3:
            st.header("Athletes")
            st.title(athletes)

        nations_over_time = helper.data_over_time(df, 'region')
        fig = px.line(nations_over_time, x="Edition", y="region")
        st.title("Participating Nations over the years")
        st.plotly_chart(fig)

        events_over_time = helper.data_over_time(df, 'Event')
        fig = px.line(events_over_time, x="Edition", y="Event")
        st.title("Events over the years")
        st.plotly_chart(fig)

        athlete_over_time = helper.data_over_time(df, 'Name')
        fig = px.line(athlete_over_time, x="Edition", y="Name")
        st.title("Athletes over the years")
        st.plotly_chart(fig)

        st.title("No. of Events over time(Every Sport)")
        fig, ax = plt.subplots(figsize=(20, 20))
        x = df.drop_duplicates(['Year', 'Sport', 'Event'])
        ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                         annot=True)
        st.pyplot(fig)

        st.title("Most successful Athletes")
        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        selected_sport = st.selectbox('Select a Sport', sport_list)
        x = helper.most_successful(df, selected_sport)
        st.table(x)

    if user_menu == 'Country-wise Analysis':
        st.sidebar.title('Country-wise Analysis')

        country_list = df['region'].dropna().unique().tolist()
        country_list.sort()

        selected_country = st.sidebar.selectbox('Select a Country', country_list)

        st.title(f"{selected_country} Medal Tally Over the Years")
        country_df = helper.yearwise_medal_tally(df, selected_country)

        if country_df.empty:
            st.warning(f"No medal data available for {selected_country}.")
        else:
            fig = px.line(country_df, x="Year", y="Medal", title=f"{selected_country} Medal Tally")
            st.plotly_chart(fig)

        st.title(f"{selected_country} Excels in the Following Sports")
        pt = helper.country_event_heatmap(df, selected_country)

        if pt.empty:
            st.warning(f"No event data available for {selected_country}.")
        else:
            fig, ax = plt.subplots(figsize=(20, 20))
            sns.heatmap(pt, annot=True, ax=ax, cmap="YlGnBu")
            ax.set_title(f"Performance of {selected_country} in Different Sports Over the Years")
            st.pyplot(fig)

        st.title(f"Top 10 Athletes of {selected_country}")
        top10_df = helper.most_successful_countrywise(df, selected_country)

        if top10_df.empty:
            st.warning(f"No athlete data available for {selected_country}.")
        else:
            st.table(top10_df)

    if user_menu == 'Athlete wise Analysis':
        athlete_df = df.drop_duplicates(subset=['Name', 'region'])

        x1 = athlete_df['Age'].dropna()
        x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
        x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
        x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

        fig = ff.create_distplot(
            [x1, x2, x3, x4],
            ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
            show_hist=False,
            show_rug=False
        )
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age")
        st.plotly_chart(fig)

        x = []
        name = []
        famous_sports = [
            'Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
            'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
            'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
            'Water Polo', 'Hockey', 'Rowing', 'Fencing',
            'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
            'Tennis', 'Golf', 'Softball', 'Archery',
            'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
            'Rhythmic Gymnastics', 'Rugby Sevens',
            'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey'
        ]
        for sport in famous_sports:
            temp_df = athlete_df[athlete_df['Sport'] == sport]
            x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
            name.append(sport)

        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.title("Distribution of Age wrt Sports (Gold Medalist)")
        st.plotly_chart(fig)

        sport_list = df['Sport'].unique().tolist()
        sport_list.sort()
        sport_list.insert(0, 'Overall')

        st.title('Height Vs Weight')
        selected_sport = st.selectbox('Select a Sport', sport_list)
        temp_df = helper.weight_v_height(df, selected_sport)

        if temp_df.empty:
            st.warning(f"No data available for {selected_sport}.")
        else:
            fig, ax = plt.subplots()
            sns.scatterplot(
                data=temp_df,
                x='Weight',
                y='Height',
                hue='Medal',
                style='Sex',
                s=60,
                ax=ax
            )
            ax.set_title(f"Height vs Weight Distribution for {selected_sport}")
            st.pyplot(fig)

        st.title("Men Vs Women Participation Over the Years")
        final = helper.men_vs_women(df)
        fig = px.line(final, x="Year", y=["Male", "Female"])
        fig.update_layout(autosize=False, width=1000, height=600)
        st.plotly_chart(fig)

else:
    st.error("Please upload athlete_events.csv to proceed.")


