# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import numpy as np
# # # # # import joblib
# # # # # import json

# # # # # # Load models & scalers
# # # # # model_cost = joblib.load("best_xgb_mc.pkl")
# # # # # scaler_cost = joblib.load("scaler_cost_mc.pkl")
# # # # # with open("features_cost.json") as f:
# # # # #     features_cost = json.load(f)

# # # # # model_dtf = joblib.load("best_xgb_dtf.pkl")
# # # # # scaler_dtf = joblib.load("scaler_dtf.pkl")
# # # # # with open("features_dtf.json") as f:
# # # # #     features_dtf = json.load(f)

# # # # # all_features = sorted(set(features_cost).union(set(features_dtf)))

# # # # # # Streamlit UI
# # # # # st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# # # # # st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# # # # # # Mode selection
# # # # # mode = st.sidebar.radio("Choose Action", ["🧮 Manual Input", "📂 Upload CSV"])

# # # # # # === Manual Mode ===
# # # # # if mode == "🧮 Manual Input":
# # # # #     st.subheader("Input Equipment Parameters")
# # # # #     input_data = {}
# # # # #     for feature in all_features:
# # # # #         input_data[feature] = st.number_input(f"{feature}", value=0.0)

# # # # #     if st.button("Predict"):
# # # # #         input_df = pd.DataFrame([input_data])
# # # # #         x_cost = scaler_cost.transform(input_df[features_cost])
# # # # #         x_dtf = scaler_dtf.transform(input_df[features_dtf])

# # # # #         cost_pred = model_cost.predict(x_cost)[0]
# # # # #         dtf_pred = model_dtf.predict(x_dtf)[0]

# # # # #         st.success(f"💸 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
# # # # #         st.success(f"⏳ **Estimated Days Till Failure:** {int(dtf_pred)} days")

# # # # # # === CSV Upload Mode ===
# # # # # elif mode == "📂 Upload CSV":
# # # # #     st.subheader("Upload CSV File")
# # # # #     file = st.file_uploader("Upload your CSV with raw features (including categorical)", type=["csv"])

# # # # #     if file is not None:
# # # # #         df = pd.read_csv(file)
# # # # #         st.write("✅ Uploaded Data Preview:", df.head())

# # # # #         # --- One-hot encode necessary categorical columns ---
# # # # #         cat_cols = df.select_dtypes(include="object").columns.tolist()
# # # # #         df_encoded = pd.get_dummies(df, columns=cat_cols)

# # # # #         # --- Align columns with model requirements ---
# # # # #         missing_cols = set(all_features) - set(df_encoded.columns)
# # # # #         for col in missing_cols:
# # # # #             df_encoded[col] = 0  # fill missing dummy with 0

# # # # #         df_encoded = df_encoded[all_features]  # reorder to match training

# # # # #         # --- Predict ---
# # # # #         x_cost = scaler_cost.transform(df_encoded[features_cost])
# # # # #         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

# # # # #         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
# # # # #         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)

# # # # #         st.success("✅ Batch prediction complete!")
# # # # #         st.dataframe(df)

# # # # #         csv = df.to_csv(index=False).encode("utf-8")
# # # # #         st.download_button("📥 Download Results", csv, "predictions.csv")


# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import numpy as np
# # # # # import joblib
# # # # # import json

# # # # # # Load models & scalers
# # # # # model_cost = joblib.load("best_xgb_mc.pkl")
# # # # # scaler_cost = joblib.load("scaler_cost_mc.pkl")
# # # # # with open("features_cost.json") as f:
# # # # #     features_cost = json.load(f)

# # # # # model_dtf = joblib.load("best_xgb_dtf.pkl")
# # # # # scaler_dtf = joblib.load("scaler_dtf.pkl")
# # # # # with open("features_dtf.json") as f:
# # # # #     features_dtf = json.load(f)

# # # # # all_features = sorted(set(features_cost).union(set(features_dtf)))

# # # # # # Streamlit UI
# # # # # st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# # # # # st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# # # # # # Mode selection
# # # # # mode = st.sidebar.radio("Choose Action", ["🧮 Manual Input", "📂 Upload CSV"])

# # # # # # === Manual Mode ===
# # # # # if mode == "🧮 Manual Input":
# # # # #     st.subheader("Input Equipment Parameters")
# # # # #     input_data = {}
# # # # #     for feature in all_features:
# # # # #         input_data[feature] = st.number_input(f"{feature}", value=0.0)

# # # # #     if st.button("Predict"):
# # # # #         input_df = pd.DataFrame([input_data])
# # # # #         x_cost = scaler_cost.transform(input_df[features_cost])
# # # # #         x_dtf = scaler_dtf.transform(input_df[features_dtf])

# # # # #         cost_pred = model_cost.predict(x_cost)[0]
# # # # #         dtf_pred = model_dtf.predict(x_dtf)[0]

# # # # #         st.success(f"💸 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
# # # # #         st.success(f"⏳ **Estimated Days Till Failure:** {int(dtf_pred)} days")

# # # # # # === CSV Upload Mode ===
# # # # # elif mode == "📂 Upload CSV":
# # # # #     st.subheader("Upload CSV File")
# # # # #     file = st.file_uploader("Upload your CSV with raw features (including categorical)", type=["csv"])

# # # # #     if file is not None:
# # # # #         df = pd.read_csv(file)
# # # # #         st.write("✅ Uploaded Data Preview:", df.head())

# # # # #         # --- One-hot encode necessary categorical columns ---
# # # # #         cat_cols = df.select_dtypes(include="object").columns.tolist()
# # # # #         df_encoded = pd.get_dummies(df, columns=cat_cols)

# # # # #         # --- Align columns with model requirements ---
# # # # #         missing_cols = set(all_features) - set(df_encoded.columns)
# # # # #         for col in missing_cols:
# # # # #             df_encoded[col] = 0  # fill missing dummy with 0

# # # # #         df_encoded = df_encoded[all_features]  # reorder to match training

# # # # #         # --- Predict ---
# # # # #         x_cost = scaler_cost.transform(df_encoded[features_cost])
# # # # #         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

# # # # #         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
# # # # #         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)

# # # # #         st.success("✅ Batch prediction complete!")
# # # # #         st.dataframe(df)

# # # # #         csv = df.to_csv(index=False).encode("utf-8")
# # # # #         st.download_button("📥 Download Results", csv, "predictions.csv")

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import numpy as np
# # # # import joblib
# # # # import json

# # # # # === Load Models & Scalers ===
# # # # model_cost = joblib.load("best_xgb_mc.pkl")
# # # # scaler_cost = joblib.load("scaler_cost_mc.pkl")
# # # # with open("features_cost.json") as f:
# # # #     features_cost = json.load(f)

# # # # model_dtf = joblib.load("best_xgb_dtf.pkl")
# # # # scaler_dtf = joblib.load("scaler_dtf.pkl")
# # # # with open("features_dtf.json") as f:
# # # #     features_dtf = json.load(f)

# # # # # === Combine All Required Features ===
# # # # all_features = sorted(set(features_cost).union(set(features_dtf)))

# # # # # === UI Setup ===
# # # # st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# # # # st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# # # # mode = st.sidebar.radio("Select Mode", ["🧮 Manual Input", "📂 Upload CSV File"])
# # # # RISK_THRESHOLD = 7  # days

# # # # # === Manual Mode ===
# # # # if mode == "🧮 Manual Input":
# # # #     st.subheader("✍️ Enter Equipment Parameters")
# # # #     input_data = {}
# # # #     for feature in all_features:
# # # #         input_data[feature] = st.number_input(f"{feature}", value=0.0)

# # # #     if st.button("🚀 Predict"):
# # # #         input_df = pd.DataFrame([input_data])

# # # #         # Predict
# # # #         x_cost = scaler_cost.transform(input_df[features_cost])
# # # #         x_dtf = scaler_dtf.transform(input_df[features_dtf])

# # # #         cost_pred = model_cost.predict(x_cost)[0]
# # # #         dtf_pred = model_dtf.predict(x_dtf)[0]
# # # #         risk = dtf_pred <= RISK_THRESHOLD

# # # #         st.success(f"💰 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
# # # #         st.success(f"📆 **Estimated Days Till Failure:** {int(dtf_pred)} days")

# # # #         if risk:
# # # #             st.error("⚠️ HIGH RISK: Equipment may fail within a week!")
# # # #         else:
# # # #             st.info("✅ Low failure risk in the next 7 days.")

# # # # # === CSV Upload Mode ===
# # # # elif mode == "📂 Upload CSV File":
# # # #     st.subheader("📁 Upload CSV File")
# # # #     uploaded_file = st.file_uploader("Upload a CSV with input features", type=["csv"])

# # # #     if uploaded_file:
# # # #         df = pd.read_csv(uploaded_file)
# # # #         st.write("📄 Preview of Uploaded Data:", df.head())

# # # #         # Encode categorical
# # # #         cat_cols = df.select_dtypes(include="object").columns.tolist()
# # # #         df_encoded = pd.get_dummies(df, columns=cat_cols)

# # # #         # Add missing dummies
# # # #         missing_cols = set(all_features) - set(df_encoded.columns)
# # # #         for col in missing_cols:
# # # #             df_encoded[col] = 0

# # # #         df_encoded = df_encoded[all_features]  # ensure correct order

# # # #         # Scale & Predict
# # # #         x_cost = scaler_cost.transform(df_encoded[features_cost])
# # # #         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

# # # #         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
# # # #         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)
# # # #         df["At_Risk_Within_7_Days"] = df["Estimated_Days_Till_Failure"] <= RISK_THRESHOLD

# # # #         # Display
# # # #         st.success("✅ Predictions Complete")
# # # #         st.dataframe(df.style.format({
# # # #             "Predicted_Maintenance_Cost": "${:.2f}",
# # # #             "Estimated_Days_Till_Failure": "{:.0f}"
# # # #         }))

# # # #         # Download results
# # # #         result_csv = df.to_csv(index=False).encode("utf-8")
# # # #         st.download_button("⬇️ Download Results CSV", result_csv, "maintenance_predictions.csv", "text/csv")

# # # #         # Summary alert
# # # #         num_risks = df["At_Risk_Within_7_Days"].sum()
# # # #         if num_risks > 0:
# # # #             st.warning(f"⚠️ {num_risks} equipment units are at risk of failure within 7 days!")
# # # #         else:
# # # #             st.success("🎉 No equipment units are predicted to fail in the next 7 days.")


# # # import streamlit as st
# # # import pandas as pd
# # # import numpy as np
# # # import joblib
# # # import json
# # # import datetime

# # # # === Load Models & Scalers ===
# # # model_cost = joblib.load("best_xgb_mc.pkl")
# # # scaler_cost = joblib.load("scaler_cost_mc.pkl")
# # # with open("features_cost.json") as f:
# # #     features_cost = json.load(f)

# # # model_dtf = joblib.load("best_xgb_dtf.pkl")
# # # scaler_dtf = joblib.load("scaler_dtf.pkl")
# # # with open("features_dtf.json") as f:
# # #     features_dtf = json.load(f)

# # # # === Combine All Required Features ===
# # # all_features = sorted(set(features_cost).union(set(features_dtf)))

# # # # === UI Setup ===
# # # st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# # # st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# # # mode = st.sidebar.radio("Select Mode", ["🧮 Manual Input", "📂 Upload CSV File"])
# # # RISK_THRESHOLD = 7  # days


# # # # === Manual Mode ===
# # # if mode == "🧮 Manual Input":
# # #     st.subheader("✍️ Enter Equipment Parameters")
# # #     input_data = {}
# # #     for feature in all_features:
# # #         input_data[feature] = st.number_input(f"{feature}", value=0.0)

# # #     if st.button("🚀 Predict"):
# # #         input_df = pd.DataFrame([input_data])

# # #         # Predict
# # #         x_cost = scaler_cost.transform(input_df[features_cost])
# # #         x_dtf = scaler_dtf.transform(input_df[features_dtf])

# # #         cost_pred = model_cost.predict(x_cost)[0]
# # #         dtf_pred = model_dtf.predict(x_dtf)[0]
# # #         risk = dtf_pred <= RISK_THRESHOLD

# # #         st.success(f"💰 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
# # #         st.success(f"📆 **Estimated Days Till Failure:** {int(dtf_pred)} days")

# # #         if risk:
# # #             st.error("⚠️ HIGH RISK: Equipment may fail within a week!")
# # #         else:
# # #             st.info("✅ Low failure risk in the next 7 days.")


# # # # === CSV Upload Mode ===
# # # elif mode == "📂 Upload CSV File":
# # #     st.subheader("📁 Upload CSV File")
# # #     uploaded_file = st.file_uploader("Upload a CSV with input features", type=["csv"])

# # #     if uploaded_file:
# # #         df = pd.read_csv(uploaded_file)
# # #         st.write("📄 Preview of Uploaded Data:", df.head())

# # #         # One-hot encode categoricals
# # #         cat_cols = df.select_dtypes(include="object").columns.tolist()
# # #         df_encoded = pd.get_dummies(df, columns=cat_cols)

# # #         # Ensure all expected features are present
# # #         missing_cols = set(all_features) - set(df_encoded.columns)
# # #         for col in missing_cols:
# # #             df_encoded[col] = 0

# # #         df_encoded = df_encoded[all_features]

# # #         # === Predictions ===
# # #         x_cost = scaler_cost.transform(df_encoded[features_cost])
# # #         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

# # #         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
# # #         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)
# # #         df["At_Risk_Within_7_Days"] = df["Estimated_Days_Till_Failure"] <= RISK_THRESHOLD

# # #         st.success("✅ Predictions Complete")
# # #         st.dataframe(df.style.format({
# # #             "Predicted_Maintenance_Cost": "${:.2f}",
# # #             "Estimated_Days_Till_Failure": "{:.0f}"
# # #         }))

# # #         # Download
# # #         result_csv = df.to_csv(index=False).encode("utf-8")
# # #         st.download_button("⬇️ Download Results CSV", result_csv, "maintenance_predictions.csv", "text/csv")

# # #         # Warning summary
# # #         num_risks = df["At_Risk_Within_7_Days"].sum()
# # #         if num_risks > 0:
# # #             st.warning(f"⚠️ {num_risks} equipment units are at risk of failure within 7 days!")
# # #         else:
# # #             st.success("🎉 No equipment units are predicted to fail in the next 7 days.")

# # #         # === Maintenance Scheduling System ===
# # #         st.markdown("## 🛠️ Maintenance Priority Schedule")

# # #         # Risk tags
# # #         def tag_risk(days):
# # #             if days <= 7:
# # #                 return "HIGH"
# # #             elif days <= 21:
# # #                 return "MEDIUM"
# # #             else:
# # #                 return "LOW"

# # #         df["Risk_Level"] = df["Estimated_Days_Till_Failure"].apply(tag_risk)
# # #         df["Suggested_Maintenance_Date"] = pd.to_datetime("today") + pd.to_timedelta(df["Estimated_Days_Till_Failure"], unit="D")
# # #         df["Suggested_Maintenance_Date"] = df["Suggested_Maintenance_Date"].dt.strftime("%Y-%m-%d %H:%M:%S")


# # #         df_schedule = df.sort_values(by="Estimated_Days_Till_Failure").copy()

# # #         # Display schedule
# # #         st.dataframe(df_schedule[[
# # #             "Equipment_ID" if "Equipment_ID" in df.columns else df.columns[0],  # fallback for nonstandard CSVs
# # #             "Estimated_Days_Till_Failure",
# # #             "Predicted_Maintenance_Cost",
# # #             "Risk_Level",
# # #             "Suggested_Maintenance_Date"
# # #         ]].style.format({
# # #             "Estimated_Days_Till_Failure": "{:.0f}",
# # #             "Predicted_Maintenance_Cost": "${:.2f}"
# # #         }))


# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import joblib
# # import json
# # import datetime

# # # === Load Models & Scalers ===
# # model_cost = joblib.load("best_xgb_mc.pkl")
# # scaler_cost = joblib.load("scaler_cost_mc.pkl")
# # with open("features_cost.json") as f:
# #     features_cost = json.load(f)

# # model_dtf = joblib.load("best_xgb_dtf.pkl")
# # scaler_dtf = joblib.load("scaler_dtf.pkl")
# # with open("features_dtf.json") as f:
# #     features_dtf = json.load(f)

# # # === Combine All Required Features ===
# # all_features = sorted(set(features_cost).union(set(features_dtf)))

# # # === UI Setup ===
# # st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# # st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# # mode = st.sidebar.radio("Select Mode", ["🧮 Manual Input", "📂 Upload CSV File"])
# # RISK_THRESHOLD = 7  # for manual mode

# # # === Manual Mode ===
# # if mode == "🧮 Manual Input":
# #     st.subheader("✍️ Enter Equipment Parameters")
# #     input_data = {}
# #     for feature in all_features:
# #         input_data[feature] = st.number_input(f"{feature}", value=0.0)

# #     if st.button("🚀 Predict"):
# #         input_df = pd.DataFrame([input_data])

# #         x_cost = scaler_cost.transform(input_df[features_cost])
# #         x_dtf = scaler_dtf.transform(input_df[features_dtf])

# #         cost_pred = model_cost.predict(x_cost)[0]
# #         dtf_pred = model_dtf.predict(x_dtf)[0]
# #         risk = dtf_pred <= RISK_THRESHOLD

# #         st.success(f"💰 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
# #         st.success(f"📆 **Estimated Days Till Failure:** {int(dtf_pred)} days")

# #         if risk:
# #             st.error("⚠️ HIGH RISK: Equipment may fail within a week!")
# #         else:
# #             st.info("✅ Low failure risk in the next 7 days.")

# # # === CSV Upload Mode ===
# # elif mode == "📂 Upload CSV File":
# #     st.subheader("📁 Upload CSV File")
# #     uploaded_file = st.file_uploader("Upload a CSV with input features", type=["csv"])

# #     if uploaded_file:
# #         df = pd.read_csv(uploaded_file)
# #         st.write("📄 Preview of Uploaded Data:", df.head())

# #         # One-hot encode categoricals
# #         cat_cols = df.select_dtypes(include="object").columns.tolist()
# #         df_encoded = pd.get_dummies(df, columns=cat_cols)

# #         # Ensure all expected features are present
# #         missing_cols = set(all_features) - set(df_encoded.columns)
# #         for col in missing_cols:
# #             df_encoded[col] = 0
# #         df_encoded = df_encoded[all_features]

# #         # === Predictions ===
# #         x_cost = scaler_cost.transform(df_encoded[features_cost])
# #         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

# #         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
# #         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)

# #         # Multi-level Risk Tags
# #         def tag_risk(days):
# #             if days <= 7:
# #                 return "🔴 HIGH"
# #             elif days <= 30:
# #                 return "🟠 MEDIUM"
# #             else:
# #                 return "🟢 LOW"

# #         df["Risk_Level"] = df["Estimated_Days_Till_Failure"].apply(tag_risk)

# #         # Suggested Maintenance Dates
# #         df["Suggested_Maintenance_Date"] = pd.to_datetime("today") + pd.to_timedelta(df["Estimated_Days_Till_Failure"], unit="D")
# #         df["Suggested_Maintenance_Date"] = df["Suggested_Maintenance_Date"].dt.strftime("%Y-%m-%d")

# #         # Final sorted schedule
# #         df_schedule = df.sort_values(by="Estimated_Days_Till_Failure").copy()

# #         # Show completed table
# #         st.success("✅ Predictions Complete")
# #         st.subheader("📋 Maintenance Priority Schedule")

# #         # Column fallback for Equipment_ID
# #         id_col = "Equipment_ID" if "Equipment_ID" in df.columns else df.columns[0]

# #         display_df = df_schedule[[
# #             id_col,
# #             "Estimated_Days_Till_Failure",
# #             "Predicted_Maintenance_Cost",
# #             "Risk_Level",
# #             "Suggested_Maintenance_Date"
# #         ]]

# #         st.dataframe(display_df.style.format({
# #             "Predicted_Maintenance_Cost": "${:.2f}",
# #             "Estimated_Days_Till_Failure": "{:.0f}"
# #         }))

# #         # Risk summary
# #         st.subheader("📊 Risk Level Summary")
# #         st.dataframe(df["Risk_Level"].value_counts().rename_axis("Risk Level").reset_index(name="Count"))

# #         # Download
# #         csv = df.to_csv(index=False).encode("utf-8")
# #         st.download_button("⬇️ Download Results CSV", csv, "maintenance_predictions.csv", "text/csv")


# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import json
# import datetime

# # === Load Models & Scalers ===
# model_cost = joblib.load("best_xgb_mc.pkl")
# scaler_cost = joblib.load("scaler_cost_mc.pkl")
# with open("features_cost.json") as f:
#     features_cost = json.load(f)

# model_dtf = joblib.load("best_xgb_dtf.pkl")
# scaler_dtf = joblib.load("scaler_dtf.pkl")
# with open("features_dtf.json") as f:
#     features_dtf = json.load(f)

# # === Combine All Required Features ===
# all_features = sorted(set(features_cost).union(set(features_dtf)))

# # === UI Setup ===
# st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
# st.title("🔧 Predict Maintenance Cost & Days Till Failure")

# mode = st.sidebar.radio("Select Mode", ["🧮 Manual Input", "📂 Upload CSV File"])
# RISK_THRESHOLD = 7  # Days to classify HIGH RISK

# # === Manual Input Mode ===
# if mode == "🧮 Manual Input":
#     st.subheader("✍️ Enter Equipment Parameters")
#     input_data = {}
#     for feature in all_features:
#         input_data[feature] = st.number_input(f"{feature}", value=0.0)

#     if st.button("🚀 Predict"):
#         input_df = pd.DataFrame([input_data])
#         x_cost = scaler_cost.transform(input_df[features_cost])
#         x_dtf = scaler_dtf.transform(input_df[features_dtf])

#         cost_pred = model_cost.predict(x_cost)[0]
#         dtf_pred = model_dtf.predict(x_dtf)[0]
#         risk = dtf_pred <= RISK_THRESHOLD

#         st.success(f"💰 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
#         st.success(f"📆 **Estimated Days Till Failure:** {int(dtf_pred)} days")

#         if risk:
#             st.error("⚠️ HIGH RISK: Equipment may fail within a week!")
#         else:
#             st.info("✅ Low failure risk in the next 7 days.")

# # === CSV Upload Mode ===
# elif mode == "📂 Upload CSV File":
#     st.subheader("📁 Upload CSV File")
#     uploaded_file = st.file_uploader("Upload a CSV with input features", type=["csv"])

#     if uploaded_file:
#         df = pd.read_csv(uploaded_file)
#         st.write("📄 Preview of Uploaded Data:", df.head())

#         # Encode categoricals
#         cat_cols = df.select_dtypes(include="object").columns.tolist()
#         df_encoded = pd.get_dummies(df, columns=cat_cols)

#         # Ensure required columns exist
#         missing_cols = set(all_features) - set(df_encoded.columns)
#         for col in missing_cols:
#             df_encoded[col] = 0

#         df_encoded = df_encoded[all_features]

#         # === Predict ===
#         x_cost = scaler_cost.transform(df_encoded[features_cost])
#         x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

#         df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
#         df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)
#         df["At_Risk_Within_7_Days"] = df["Estimated_Days_Till_Failure"] <= RISK_THRESHOLD

#         # === Maintenance Risk Level ===
#         def tag_risk(days):
#             if days <= 7:
#                 return "🔴 HIGH"
#             elif days <= 21:
#                 return "🟠 MEDIUM"
#             else:
#                 return "🟢 LOW"

#         df["Risk_Level"] = df["Estimated_Days_Till_Failure"].apply(tag_risk)
#         # df["Suggested_Maintenance_Date"] = pd.to_datetime("today") + pd.to_timedelta(df["Estimated_Days_Till_Failure"], unit="D")
#         # df["Suggested_Maintenance_Date"] = df["Suggested_Maintenance_Date"].dt.strftime("%Y-%m-%d %H:%M:%S")

#         # === Cost Opportunity Tag ===
#         COST_THRESHOLD = df["Predicted_Maintenance_Cost"].quantile(0.2)

#         def tag_cost_opportunity(row):
#             if row["Risk_Level"] != "🔴 HIGH" and row["Predicted_Maintenance_Cost"] <= COST_THRESHOLD:
#                 return "💸 Cost-Optimized Opportunity"
#             return ""

#         df["Cost_Opportunity_Tag"] = df.apply(tag_cost_opportunity, axis=1)

#         # === Display Results ===
#         st.success("✅ Predictions Complete")

#         st.dataframe(df.style.format({
#             "Predicted_Maintenance_Cost": "${:.2f}",
#             "Estimated_Days_Till_Failure": "{:.0f}"
#         }))

#         # === Download Results ===
#         result_csv = df.to_csv(index=False).encode("utf-8")
#         st.download_button("⬇️ Download Results CSV", result_csv, "maintenance_predictions.csv", "text/csv")

#         # === Risk Alert Summary ===
#         num_risks = df["At_Risk_Within_7_Days"].sum()
#         if num_risks > 0:
#             st.warning(f"⚠️ {num_risks} equipment units are at risk of failure within 7 days!")
#         else:
#             st.success("🎉 No equipment units are predicted to fail in the next 7 days.")

#         # === Maintenance Priority Schedule ===
#         st.markdown("## 🛠️ Maintenance Priority Schedule")

#         schedule_cols = [
#             "Equipment_ID" if "Equipment_ID" in df.columns else df.columns[0],
#             "Estimated_Days_Till_Failure",
#             "Predicted_Maintenance_Cost",
#             "Risk_Level",
#             "Cost_Opportunity_Tag",
#             #"Suggested_Maintenance_Date"
#         ]

#         df_schedule = df.sort_values(by="Estimated_Days_Till_Failure").copy()

#         st.dataframe(df_schedule[schedule_cols].style.format({
#             "Estimated_Days_Till_Failure": "{:.0f}",
#             "Predicted_Maintenance_Cost": "${:.2f}"
#         }))


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import datetime

# === Load Models & Scalers ===
model_cost = joblib.load("best_xgb_mc.pkl")
scaler_cost = joblib.load("scaler_cost_mc.pkl")
with open("features_cost.json") as f:
    features_cost = json.load(f)

model_dtf = joblib.load("best_xgb_dtf.pkl")
scaler_dtf = joblib.load("scaler_dtf.pkl")
with open("features_dtf.json") as f:
    features_dtf = json.load(f)

# === Combine All Required Features ===
all_features = sorted(set(features_cost).union(set(features_dtf)))

# === UI Setup ===
st.set_page_config(page_title="Maintenance & Failure Predictor", layout="centered")
st.title("🔧 Predict Maintenance Cost & Days Till Failure")

mode = st.sidebar.radio("Select Mode", ["🧮 Manual Input", "📂 Upload CSV File"])
RISK_THRESHOLD = 7  # Days to classify HIGH RISK

# === Manual Input Mode ===
if mode == "🧮 Manual Input":
    st.subheader("✍️ Enter Equipment Parameters")
    input_data = {}
    for feature in all_features:
        input_data[feature] = st.number_input(f"{feature}", value=0.0)

    if st.button("🚀 Predict"):
        input_df = pd.DataFrame([input_data])
        x_cost = scaler_cost.transform(input_df[features_cost])
        x_dtf = scaler_dtf.transform(input_df[features_dtf])

        cost_pred = model_cost.predict(x_cost)[0]
        dtf_pred = model_dtf.predict(x_dtf)[0]
        risk = dtf_pred <= RISK_THRESHOLD

        st.success(f"💰 **Predicted Maintenance Cost:** ${cost_pred:,.2f}")
        st.success(f"📆 **Estimated Days Till Failure:** {int(dtf_pred)} days")

        if risk:
            st.error("⚠️ HIGH RISK: Equipment may fail within a week!")
        else:
            st.info("✅ Low failure risk in the next 7 days.")

# === CSV Upload Mode ===
elif mode == "📂 Upload CSV File":
    st.subheader("📁 Upload CSV File")
    uploaded_file = st.file_uploader("Upload a CSV with input features", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Preview of Uploaded Data:", df.head())

        # Save Equipment_ID separately for display
        equipment_ids = df["Equipment_ID"] if "Equipment_ID" in df.columns else None

        # Drop Equipment_ID before encoding
        if "Equipment_ID" in df.columns:
            df = df.drop(columns=["Equipment_ID"])

        # Encode categoricals
        cat_cols = df.select_dtypes(include="object").columns.tolist()
        df_encoded = pd.get_dummies(df, columns=cat_cols)

        # Ensure required columns exist
        missing_cols = set(all_features) - set(df_encoded.columns)
        for col in missing_cols:
            df_encoded[col] = 0

        df_encoded = df_encoded[all_features]

        # === Predict ===
        x_cost = scaler_cost.transform(df_encoded[features_cost])
        x_dtf = scaler_dtf.transform(df_encoded[features_dtf])

        df["Predicted_Maintenance_Cost"] = model_cost.predict(x_cost)
        df["Estimated_Days_Till_Failure"] = model_dtf.predict(x_dtf)
        df["At_Risk_Within_7_Days"] = df["Estimated_Days_Till_Failure"] <= RISK_THRESHOLD

        # === Maintenance Risk Level ===
        def tag_risk(days):
            if days <= 7:
                return "🔴 HIGH"
            elif days <= 21:
                return "🟠 MEDIUM"
            else:
                return "🟢 LOW"

        df["Risk_Level"] = df["Estimated_Days_Till_Failure"].apply(tag_risk)

        # === Cost Opportunity Tag ===
        COST_THRESHOLD = df["Predicted_Maintenance_Cost"].quantile(0.2)

        def tag_cost_opportunity(row):
            if row["Risk_Level"] != "🔴 HIGH" and row["Predicted_Maintenance_Cost"] <= COST_THRESHOLD:
                return "💸 Cost-Optimized Opportunity"
            return ""

        df["Cost_Opportunity_Tag"] = df.apply(tag_cost_opportunity, axis=1)

        # Re-attach Equipment_ID for display (if available)
        if equipment_ids is not None:
            df.insert(0, "Equipment_ID", equipment_ids)

        # === Display Results ===
        st.success("✅ Predictions Complete")
        st.dataframe(df.style.format({
            "Predicted_Maintenance_Cost": "${:.2f}",
            "Estimated_Days_Till_Failure": "{:.0f}"
        }))

        # === Download Results ===
        result_csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Results CSV", result_csv, "maintenance_predictions.csv", "text/csv")

        # === Risk Alert Summary ===
        num_risks = df["At_Risk_Within_7_Days"].sum()
        if num_risks > 0:
            st.warning(f"⚠️ {num_risks} equipment units are at risk of failure within 7 days!")
        else:
            st.success("🎉 No equipment units are predicted to fail in the next 7 days.")

        # === Maintenance Priority Schedule ===
        st.markdown("## 🛠️ Maintenance Priority Schedule")

        schedule_cols = [
            "Equipment_ID" if "Equipment_ID" in df.columns else df.columns[0],
            "Estimated_Days_Till_Failure",
            "Predicted_Maintenance_Cost",
            "Risk_Level",
            "Cost_Opportunity_Tag"
        ]

        df_schedule = df.sort_values(by="Estimated_Days_Till_Failure").copy()

        st.dataframe(df_schedule[schedule_cols].style.format({
            "Estimated_Days_Till_Failure": "{:.0f}",
            "Predicted_Maintenance_Cost": "${:.2f}"
        }))

# Custom Footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    </style>
    <div class="footer">
        Developed by Oluwakemi - ©2025
        <br>
        <a href="https://www.linkedin.com/in/oluwakemi-sorinmade/" target="_blank">LinkedIn</a>
        <a href="https://github.com/Olukem" target="_blank">GitHub</a>
    </div>
    """, unsafe_allow_html=True)