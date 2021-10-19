<?php
/**
 * La configuration de base de votre installation WordPress.
 *
 * Ce fichier est utilisé par le script de création de wp-config.php pendant
 * le processus d’installation. Vous n’avez pas à utiliser le site web, vous
 * pouvez simplement renommer ce fichier en « wp-config.php » et remplir les
 * valeurs.
 *
 * Ce fichier contient les réglages de configuration suivants :
 *
 * Réglages MySQL
 * Préfixe de table
 * Clés secrètes
 * Langue utilisée
 * ABSPATH
 *
 * @link https://fr.wordpress.org/support/article/editing-wp-config-php/.
 *
 * @package WordPress
 */

// ** Réglages MySQL - Votre hébergeur doit vous fournir ces informations. ** //
/** Nom de la base de données de WordPress. */
define( 'DB_NAME', 'wpbdd' );

/** Utilisateur de la base de données MySQL. */
define( 'DB_USER', 'wpid' );

/** Mot de passe de la base de données MySQL. */
define( 'DB_PASSWORD', 'temp' );

/** Adresse de l’hébergement MySQL. */
define( 'DB_HOST', 'database' );

/** Jeu de caractères à utiliser par la base de données lors de la création des tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/**
 * Type de collation de la base de données.
 * N’y touchez que si vous savez ce que vous faites.
 */
define( 'DB_COLLATE', '' );

/**#@+
 * Clés uniques d’authentification et salage.
 *
 * Remplacez les valeurs par défaut par des phrases uniques !
 * Vous pouvez générer des phrases aléatoires en utilisant
 * {@link https://api.wordpress.org/secret-key/1.1/salt/ le service de clés secrètes de WordPress.org}.
 * Vous pouvez modifier ces phrases à n’importe quel moment, afin d’invalider tous les cookies existants.
 * Cela forcera également tous les utilisateurs à se reconnecter.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'n(k[0G3=}+76=FEiR$CbJY9E^qrpTNFu-UaL{G:R4OiH$b:wz]>jGZC$FFGa*Q92' );
define( 'SECURE_AUTH_KEY',  '#7~UDn#xGX=38W>RTf8TKf:0;46XF%`1Jg;z.2Tk6*p>O>lLr~6;|#mO!<8@T0,o' );
define( 'LOGGED_IN_KEY',    '_jo>iD4y?6d0J{lC.zo$L|gPty1q_4-xaeEwK49v@dr~r:zC21SDd5%Yq?)uh@{f' );
define( 'NONCE_KEY',        'UoIt$T9@dV1B4@dv9Z^`;w8eT/!@fC1@G9@run,#MXOP=nV<[f{It{&9Sge]gVIh' );
define( 'AUTH_SALT',        'mAIAY;.Ai<c?G34uH[o9.4,ghx?h=,-r^dZa)-NaLxFK);5&#0+0wA*U9thm.|3n' );
define( 'SECURE_AUTH_SALT', '^pmsW-_=o:+E-`;VL,B:QdmFHo-_3mwe_s8#-lLh3sGd .u8W03i^xC,~Ns?9Mj!' );
define( 'LOGGED_IN_SALT',   'r4/&Y^2fDK?2&7oOm1E6ad5qM70*p`@8+6Fbw;2u!xe/`F*}BjsvDf!ExN)Hm]3h' );
define( 'NONCE_SALT',       'Kl,<nnM|f]jORDtcXl1/`O[`Nsl(>z<{s`-<HbVONT90^p J49xlfrVidEdTdz^?' );
/**#@-*/

/**
 * Préfixe de base de données pour les tables de WordPress.
 *
 * Vous pouvez installer plusieurs WordPress sur une seule base de données
 * si vous leur donnez chacune un préfixe unique.
 * N’utilisez que des chiffres, des lettres non-accentuées, et des caractères soulignés !
 */
$table_prefix = 'wp_';

/**
 * Pour les développeurs : le mode déboguage de WordPress.
 *
 * En passant la valeur suiwante à "true", vous activez l’affichage des
 * notifications d’erreurs pendant vos essais.
 * Il est fortement recommandé que les développeurs d’extensions et
 * de thèmes se servent de WP_DEBUG dans leur environnement de
 * développement.
 *
 * Pour plus d’information sur les autres constantes qui peuvent être utilisées
 * pour le déboguage, rendez-vous sur le Codex.
 *
 * @link https://fr.wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', true );

/* C’est tout, ne touchez pas à ce qui suit ! Bonne publication. */

/** Chemin absolu vers le dossier de WordPress. */
if ( ! defined( 'ABSPATH' ) )
  define( 'ABSPATH', dirname( __FILE__ ) . '/' );

/** Réglage des variables de WordPress et de ses fichiers inclus. */
require_once( ABSPATH . 'wp-settings.php' );
