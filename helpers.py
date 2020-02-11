# Nonlinear Transfrom Shiz
def nonLinearTransform(df0, train=False):
    df = df0.copy()
    # Reset y's to regression target
    bid_diffs = pd.DataFrame({f'bid_w{i}': ((df[f'bid{i}'] - df['mid']) * df[f'bid{i}vol']) \
                              for i in range(1, 6)})
    ask_diffs = pd.DataFrame({f'ask_w{i}': ((df[f'ask{i}'] - df['mid']) * df[f'ask{i}vol']) \
                              for i in range(1, 6)})
    drop_cols = [f'{a}{b}{c}' for a in ['bid', 'ask'] for b in range(1, 6) for c in ["", "vol"]] + \
                ['id'] + (['y'] if train else [])
    df = df.drop(drop_cols, axis = 1).join(bid_diffs).join(ask_diffs)
    if train:
        df['y'] = list(df0['mid'].values[2:] - df0['mid'].values[:-2]) + list(df0['y'].values[-2:])
    return df

train_df = nonLinearTransform(pd.read_csv('train.csv'), train=True)
train_df.head(5)

# AUROC
from sklearn.metrics import roc_auc_score as auc
clf.fit(X, Y)
Y_fake = clf.predict(valX)
auc(valY, Y_fake)
